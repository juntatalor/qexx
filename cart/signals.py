__author__ = 'Сергей'

from django.dispatch import Signal

# Сигналы
checkout_form_init_start = Signal(providing_args=['instance'])
checkout_form_init_done = Signal(providing_args=['instance'])
