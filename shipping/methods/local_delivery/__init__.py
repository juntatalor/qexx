__author__ = 'Сергей'

from shipping.methods import BaseShipment
from django import forms


class LocalDelivery(BaseShipment):

    id = 'LocalDelivery'
    name = 'Курьерская доставка'
    help_text = 'Курьерская доставка по Москве'

    def get_price(self):
        # Расчет стоимости доставки в зависимости от стоимости корзины
        # if not self.cart:
        #    return 400
        total_price = self.checkout_form.cart.get_cart_summary()['cart_price']
        if 0 <= total_price < 1499:
            return 400
        elif 1500 <= total_price < 2499:
            return 200
        else:
            return 0

    @classmethod
    def update_form(cls, form):
        form.fields['address'] = forms.CharField(label='Адрес',
                                                 widget=forms.Textarea(
                                                     attrs={'placeholder': 'Введите полный адрес'}))
        form.shipping_data = [
            form['address']
        ]
        # Удаление недопустимых методов оплаты
        forbidden_gateways = ['CashOnDelivery']
        form.fields['payment'].choices = \
            [(name, v) for name, v in form.fields['payment'].choices if name not in forbidden_gateways]


METHOD = LocalDelivery
