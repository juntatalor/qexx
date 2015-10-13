__author__ = 'Сергей'

from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        # загрузка сигналов
        from stock import signals
