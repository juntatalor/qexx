__author__ = 'Сергей'

from cart.utils import get_cart


def user_cart(request):
    cart, created = get_cart(request, False)
    return {'user_cart': cart}