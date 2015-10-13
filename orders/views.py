from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce
from django.db.models import Sum, F
from django.views.decorators.http import require_GET

from orders.models import Order, OrderProducts
from orders.constants import PAYMENT_STATUS
from shipping.methods import methods
from payment.gateways import gateways


# Create your views here.


@require_GET
def direct_view(request, uid):
    try:
        order = Order.objects.get(uid=uid)
    except Order.DoesNotExist:
        return HttpResponseBadRequest('Wrong parameters')

    new_order = 'new_order' in request.GET

    payment_method = gateways[order.payment_method]
    if payment_method.online_payment and order.payment_status != PAYMENT_STATUS['PAYED']:
        payment_url = payment_method.get_payment_url(order)
    else:
        payment_url = ''

    return render(request, 'orders/order.html', {
        'order': order,
        'new_order': new_order,
        'payment_url': payment_url,
        'payment_method': payment_method.name,
        'shipping_method': methods[order.shipping_method].name,
        'order_products': OrderProducts.objects.filter(order=order).
                  select_related('priced_product__product')
    })


@login_required
@require_GET
def order_index(request):
    order_list = Order.objects. \
        filter(user=request.user). \
        annotate(amount_sum=Coalesce(Sum('order_products__amount'), 0),
                 price_sum=Coalesce(Sum(F('order_products__price') * F('order_products__amount')), 0))
    return render(request, 'orders/order_list.html', {'order_list': order_list})


@require_GET
def print_cheque(request):
    try:
        order = Order.objects.get(pk=request.GET['order_id'])
    except (KeyError, Order.DoesNotExist):
        return HttpResponseBadRequest('Wrong parameters')

    payment_method = gateways[order.payment_method]
    shipping_method = methods[order.shipping_method]

    return render(request, 'orders/print/cheque.html', {'order': order,
                                                        'payment_method': payment_method,
                                                        'shipping_method': shipping_method})