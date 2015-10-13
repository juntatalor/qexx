__author__ = 'Сергей'

from phonenumbers import parse, format_number, PhoneNumberFormat, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException

from django.core.exceptions import ValidationError

from shipping.models import Country

class PhoneValidator(object):
    def __init__(self, country=None):
        try:
            self.country = Country.objects.get(pk=int(country))
        except (ValueError, KeyError, TypeError, Country.DoesNotExist):
            self.country = Country.default_country()

    def __call__(self, value):
        try:
            number = parse(value, self.country.code_a2)
        except NumberParseException:
            raise ValidationError('Введен некорректный номер телефона')

        if is_valid_number(number):
            return format_number(number, PhoneNumberFormat.NATIONAL)
        else:
            raise ValidationError('Введен некорректный номер телефона')