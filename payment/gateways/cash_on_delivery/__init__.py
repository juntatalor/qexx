__author__ = 'Сергей'

from payment.gateways import BaseGateway


class CashOnDelivery(BaseGateway):
    id = 'CashOnDelivery'
    name = 'Наложенный платеж'
    help_text = 'Лучший платеж почтой России'


GATEWAY = CashOnDelivery
