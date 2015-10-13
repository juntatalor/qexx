__author__ = 'Сергей'

from django.utils.crypto import get_random_string
from cart.models import Cart


def get_cart(request, create=True):
    # При смене пользователя сначала переносится корзина
    # (см. cart.apps)

    # Проверим, создалась ли сессия
    if not request.session.session_key:
        request.session.create()

    # UID корзины хранится в сессии
    uid = request.session.get('cart_uid', None)
    # Проверим, аутентифицирован ли пользователь
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None

    if create:
        # Создание UID при необходимости
        if not uid:
            uid = get_random_string(32)
            request.session['cart_uid'] = uid
            if user:
                return Cart.objects.update_or_create(owner=user,
                                                     defaults={'uid': uid})
        cart, created = Cart.objects.update_or_create(uid=uid,
                                                      defaults={'owner': user})
    else:
        created = False
        cart = None
        try:
            if uid:
                cart = Cart.objects.get(uid=uid)
            elif user:
                cart = Cart.objects.get(owner=user)
        except Cart.DoesNotExist:
            cart = None

    return cart, created
