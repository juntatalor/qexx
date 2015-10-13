__author__ = 'Сергей'

from django.dispatch import receiver

from stock.utils import create_sr_main, create_sr_additional
from orders.signals import order_post_save


@receiver(order_post_save)
def signal_create_sr(sender, instance, **kwargs):
    # Запись списаний для заказа
    create_sr_main(instance)
    create_sr_additional(instance)
