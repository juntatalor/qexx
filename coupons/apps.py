__author__ = 'Сергей'

from django.apps import AppConfig


class CouponsConfig(AppConfig):
    name = 'coupons'

    def ready(self):
        # загрузка сигналов
        from coupons import signals
