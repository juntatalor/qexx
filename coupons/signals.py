__author__ = 'Сергей'

from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from coupons.utils import copy_cart_coupons_to_order, set_cart_discount
from cart.signals import checkout_form_init_done


@receiver(post_save, sender=Order)
def signal_order_coupons(sender, **kwargs):
    # Копирование купонов из корзины
    order = kwargs['instance']
    copy_cart_coupons_to_order(order.cart, order)


@receiver(checkout_form_init_done)
def signal_apply_coupons(sender, **kwargs):
    # Применение скидки к чекауту
    form = kwargs['instance']
    set_cart_discount(form)





