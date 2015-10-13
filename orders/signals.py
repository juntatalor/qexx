__author__ = 'Сергей'

from django.dispatch import Signal

# Сигналы
order_post_save = Signal(providing_args=['instance'])
