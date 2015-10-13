__author__ = 'Сергей'

from payment.gateways import BaseGateway


class Cash(BaseGateway):
    id = 'Cash'
    name = 'Оплата наличными'
    help_text = 'Оплата наличными при получении. Просто и понятно - ведь деньги не пахнут.'
    

GATEWAY = Cash