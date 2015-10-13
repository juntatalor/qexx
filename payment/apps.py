__author__ = 'Сергей'

from importlib import import_module
from collections import OrderedDict

from django.apps import AppConfig
from django.conf import settings

import payment.gateways


class PaymentConfig(AppConfig):
    name = 'payment'

    def ready(self):
        gateways = []
        for payment_method in settings.PAYMENT_CLASSES:
            try:
                module = import_module(payment_method)
                gateway = getattr(module, 'GATEWAY', None)
                if issubclass(gateway, payment.gateways.BaseGateway):
                    gateways.append((gateway.id, gateway))
            except (ImportError, TypeError):
                raise ImportError('Ошибка загрузки: ' + payment_method)
        payment.gateways.gateways = OrderedDict(gateways)