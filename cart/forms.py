__author__ = 'Сергей'

from django import forms
from django.forms.widgets import RadioFieldRenderer, RadioSelect
from django.forms.utils import ErrorList
from django.forms import ValidationError
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.auth import get_user_model

from common.validators import PhoneValidator
from shipping.methods import methods, initial_method
from payment.gateways import gateways
from cart.signals import checkout_form_init_done, checkout_form_init_start


class CartRadioChoiceFieldRenderer(RadioFieldRenderer):
    def render(self):
        # Убрана возможность делать вложенные списки choices=('Test lv 1',[('Test lv 2', 'Test val')])
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<ul id="{0}">', id_) if id_ else '<ul>'
        output = [start_tag]
        for i, choice in enumerate(self.choices):
            choice_value = choice[1]
            output.append(format_html('<li>{0}</li>', choice_value.render(self, i)))
        output.append('</ul>')
        return mark_safe('\n'.join(output))


class CartRadioSelect(RadioSelect):
    renderer = CartRadioChoiceFieldRenderer


class CheckoutForm(forms.Form):
    # Поля формы

    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'placeholder': 'Иван'}))
    last_name = forms.CharField(label='Фамилия',
                                required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Иванов'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'ivanov@example.ru'}))

    # Предложение зарегистрироваться для незарегистрированных пользователей
    register = forms.BooleanField(label='Зарегистрироваться', required=False)

    def clean_email(self):
        # Если пользователь не залогинился, то такого емейла не должно быть в базе
        user_model = get_user_model()
        email = self.cleaned_data['email']
        # "Обратное" использование try ... except:
        # При ошибке (нет email в базе) возвращается значение
        # При нормальном выполнении (есть email в базе) возвращается ошибка
        try:
            user = user_model.objects.get(email__iexact=email)
            if user != self.user:
                raise ValidationError('Этот email уже используется зарегистрированным пользователем')
            return email
        except user_model.DoesNotExist:
            return email

    def __init__(self, cart, user, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False):

        checkout_form_init_start.send(sender=self.__class__, instance=self)

        # Получаем мутабельную версию начальных значений
        from django.http import QueryDict

        if isinstance(initial, QueryDict):
            initial = initial.copy()

        # Заполнение начальных значений по профилю пользователя
        if user and initial is not None:
            # ToDo: по всей вероятности это можно сделать more pythonic
            initial['country'] = user.country
            initial['address'] = user.address
            initial['phone'] = user.phone
            initial['first_name'] = user.first_name
            initial['last_name'] = user.last_name
            initial['middle_name'] = user.middle_name
            initial['email'] = user.email

        super(CheckoutForm, self).__init__(data, files, auto_id, prefix,
                                           initial, error_class, label_suffix,
                                           empty_permitted)
        self.user = user
        self.cart = cart

        self.fields['phone'] = forms.CharField(label='Телефон', validators=[PhoneValidator(self.data.get('country', None))])

        # Добавление полей оплаты и доставки
        self.fields['payment'] = forms.ChoiceField(label='Оплата',
                                                   choices=[(name, gw()) for name, gw in gateways.items()],
                                                   widget=CartRadioSelect)

        self.fields['shipment'] = forms.ChoiceField(label='Доставка',
                                                    choices=[(name, mt(checkout_form=self)) for name, mt in methods.items()],
                                                    widget=CartRadioSelect)

        # Обращение к Form.__getitem__ для получения BoundField
        self.personal_data = [
            self['first_name'], self['last_name'], self['email'], self['phone']
        ]

        self.shipping_data = []

        # Обработка формы с учетом выбранной доставки и оплаты (initial - Ajax запрос, data - валидация формы)
        shipment = self.initial.get('shipment', self.data.get('shipment', None))
        payment = self.initial.get('payment', self.data.get('payment', None))

        if shipment in methods:
            shipping_method = methods[shipment](checkout_form=self)
        else:
            shipping_method = initial_method(checkout_form=self)
        shipping_method.update_form(self)
        self.shipping_method = shipping_method
        # Установка метода оплаты по умолчанию для данного метода доставки
        self.initial['payment'] = shipping_method.initial_gateway

        if payment in gateways:
            payment_gateway = gateways[payment]()
        else:
            payment_gateway = gateways[shipping_method.initial_gateway]()
        payment_gateway.update_form(self)
        self.payment_gateway = payment_gateway

        cart_price = cart.get_cart_summary()['cart_price']
        shipping_price = shipping_method.get_price()
        self._cart_summary = {
            'shipping_price': shipping_price,
            'cart_price': cart_price,
            'total_price': cart_price + shipping_price,
            'final_price': cart_price + shipping_price
        }

        checkout_form_init_done.send(sender=self.__class__, instance=self)

    @property
    def cart_summary(self):
        return self._cart_summary
