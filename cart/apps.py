__author__ = 'Сергей'

from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in


class CartConfig(AppConfig):
    name = 'cart'

    def ready(self):
        user_logged_in.connect(move_cart)


def move_cart(sender, user, request, **kwargs):
    """
    Если после логина корзина пользователя не пустая,
    удаляет старую корзину пользователя и использует корзину из сохраненной сессии
    :param sender:
    :param user:
    :param request:
    :param kwargs:
    :return:
    """
    uid = request.session.get('cart_uid', None)
    if uid:
        from cart.models import Cart
        Cart.objects.filter(uid=uid).update(owner=user)
        Cart.objects.filter(owner=user).\
            exclude(uid=uid).\
            delete()
