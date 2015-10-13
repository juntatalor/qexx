__author__ = 'Сергей'

from importlib import import_module
from collections import OrderedDict

from django.apps import AppConfig
from django.conf import settings

import shipping.methods


class ShippingConfig(AppConfig):
    name = 'shipping'

    def ready(self):
        methods = []
        for shipping_method in settings.SHIPPING_CLASSES:
            try:
                module = import_module(shipping_method)
                method = getattr(module, 'METHOD', None)
                if issubclass(method, shipping.methods.BaseShipment):
                    methods.append((method.id, method))
            except (ImportError, TypeError):
                raise ImportError('Ошибка загрузки: ' + shipping_method)
        shipping.methods.methods = OrderedDict(methods)
        shipping.methods.initial_method = shipping.methods.methods['PickupDelivery']