__author__ = 'Сергей'

from coupons.models import Coupon
from django.utils import timezone
from django.db.models import Count


def set_order_discount(order):
    """
    Функция возвращает скидки по купонам для заказа
    :param order:
    :return:
    """
    return get_discount(Coupon.objects.filter(orders=order),
                        order.get_order_summary()['price'])


def set_cart_discount(checkout_form):
    """
    Функция возвращает скидки по купонам для корзины
    :param checkout_from:
    :param result:
    :return:
    """
    cart = checkout_form.cart
    cart_discount, free_delivery = get_discount(Coupon.objects.filter(carts=cart),
                                                checkout_form.cart_summary['cart_price'])
    if free_delivery and checkout_form.shipping_method.free_delivery_available:
        shipping_discount = checkout_form.cart_summary['shipping_price']
    else:
        shipping_discount = 0

    checkout_form.cart_summary['discount'] = cart_discount
    checkout_form.cart_summary['shipping_price'] -= shipping_discount
    checkout_form.cart_summary['total_price'] -= shipping_discount
    checkout_form.cart_summary['final_price'] -= shipping_discount + cart_discount


def get_discount(coupons, summ):
    discount_fix = 0
    discount_percent = 0
    discount_free_delivery = False

    for coupon in coupons:
        discount_fix += coupon.discount_fix
        discount_percent += coupon.discount_percent
        if coupon.discount_free_delivery:
            discount_free_delivery = True

    discount_percent = max(discount_percent, 0)
    discount_fix = min(discount_fix, summ)

    return discount_fix + (summ - discount_fix) * discount_percent / 100, \
           discount_free_delivery


def coupon_valid(coupon):
    # Купон должен быть:
    # 1) Активным
    # 2) Бессрочным, либо с неистекшим сроком действия
    # 3) Дата начала использования купона должна наступить
    # 4) Не использован максимальное число раз
    usages = Coupon.objects.filter(pk=coupon.id). \
        aggregate(count=Count('orders'))
    return coupon.active \
           and (coupon.expire_date is None
                or coupon.expire_date >= timezone.now()) \
           and (coupon.date is None
                or coupon.date <= timezone.now()) \
           and (coupon.max_usage == 0
                or usages['count'] < coupon.max_usage)


def get_cart_coupons(cart):
    return Coupon.objects.filter(carts=cart)


def copy_cart_coupons_to_order(cart, order):
    for coupon in get_cart_coupons(cart):
        coupon.orders.add(order)
