__author__ = 'Сергей'

from django import template

from coupons.utils import get_cart_coupons

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_coupons(context):
    cart = context['user_cart']
    return get_cart_coupons(cart)
