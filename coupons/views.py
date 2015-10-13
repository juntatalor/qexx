from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.template import RequestContext

from coupons.models import Coupon
from coupons.utils import coupon_valid
from cart.utils import get_cart


# Ajax методы для работы с купонами в корзине

@require_POST
def add_coupon(request):
    coupon = get_coupon(request)
    result = {}

    if coupon is None or not coupon_valid(coupon):
        result['error'] = 'Неверный код купона'
        return JsonResponse(result)

    cart, created = get_cart(request)
    coupon.carts.add(cart)
    result['html'] = render_to_string('coupons/cart_coupons_form.html',
                                      {'cart_coupons': Coupon.objects.filter(carts=cart)},
                                      context_instance=RequestContext(request))
    return JsonResponse(result)


@require_POST
def remove_coupon(request):
    coupon = get_coupon(request)
    result = {}

    if coupon is None:
        result['error'] = 'Неверный код купона'
        return JsonResponse(result)

    cart, created = get_cart(request)
    coupon.carts.remove(cart)
    result['html'] = render_to_string('coupons/cart_coupons_form.html',
                                      {'cart_coupons': Coupon.objects.filter(carts=cart)},
                                      context_instance=RequestContext(request))
    return JsonResponse(result)


def get_coupon(request):
    try:
        return Coupon.objects.get(code=request.POST['coupon'])
    except (KeyError, Coupon.DoesNotExist):
        return None
