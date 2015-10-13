__author__ = 'Сергей'

from django import forms

from shipping.models import Country
from shipping.methods import BaseShipment

import zlib
import urllib
import json

class PostDelivery(BaseShipment):
    id = 'PostDelivery'
    name = 'Доставка почтой России'
    help_text = 'Самая скоростная доставка на свете в страны таможенного союза'
    initial_gateway = 'CashOnDelivery'
    free_delivery_available = False

    def get_price(self, **kwargs):
        # Сервер API:
        api_request = "http://test.postcalc.ru/?f=%s&t=%s&o=JSON"
        # Стоимость доставки при возникновении ошибки:
        error_price = 400
        sender_zip = self.checkout_form.data.get('zip', '')
        # Тип отправления. Да, ключ массива строка на Русском языке.
        delivery_type = "ЦеннаяАвиаПосылка_Difficult"
        receiver_zip = self.checkout_form.data.get('zip')
        if receiver_zip is None or len(receiver_zip) == 0:
            # return True, error_price
            # Пока вызов этой функции не умеет обрабатывать ошибки
            return error_price

        response = urllib.request.urlopen(api_request % (sender_zip, receiver_zip))
        decompressed_data = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS)
        obj = json.loads(decompressed_data.decode())
        # ToDo: разбор json
        # return False, 300
        return 300

    @classmethod
    def update_form(cls, form):
        # Добавление новых полей
        form.fields['middle_name'] = forms.CharField(label='Отчество',
                                                     widget=forms.TextInput(attrs={'placeholder': 'Иванович'}))
        form.personal_data.insert(2, form['middle_name'])
        # Поля с адресом доставки
        # Доступные страны
        available_countries = ['РОССИЯ', 'КАЗАХСТАН', 'БЕЛАРУСЬ', 'АРМЕНИЯ', 'КИРГИЗИЯ']
        form.fields['country'] = forms.ModelChoiceField(label='Страна',
                                                        initial=Country.default_country(),
                                                        queryset=Country.objects.filter(name__in=available_countries))
        form.fields['zip'] = forms.CharField(label='Индекс',
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Индекс'}))
        form.fields['region'] = forms.CharField(label='Населённый пункт',
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Введите название города, деревни, посёлка'}))
        form.fields['address'] = forms.CharField(label='Адрес доставки',
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Введите оставшуюся часть адреса доставки'}))
        form.fields['last_name'].required = True

        form.shipping_data = [
            form['country'], form['zip'], form['region'], form['adddress']
        ]
        # Удаление недопустимых методов оплаты
        forbidden_gateways = ['Cash']
        form.fields['payment'].choices = \
            [(name, v) for name, v in form.fields['payment'].choices if name not in forbidden_gateways]


METHOD = PostDelivery
