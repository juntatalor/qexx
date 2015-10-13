import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db import transaction
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.template.loader import render_to_string
from django.template import RequestContext

from cart.models import CartProducts
from cart.forms import CheckoutForm
from cart.utils import get_cart
from products.models import PricedProduct
from shipping.methods import initial_method
from orders.utils import create_new_order
from accounts.utils import register_user, send_registration_email

# AJAX запросы


@require_POST
def add_to_cart(request):
    priced_product = get_product(request)
    amount = get_amount(request)

    if None in [priced_product, amount]:
        return HttpResponseBadRequest('Wrong parameters')

    # Корзина
    cart, created = get_cart(request)

    result = {}

    # Проверим, нет заказывается ли больше, чем есть в наличии + есть в корзине
    if priced_product.product.stock_track != priced_product.product.STOCK_AVAILABLE:
        try:
            cart_amount = CartProducts.objects.get(cart=cart,
                                                   priced_product=priced_product).amount
        except CartProducts.DoesNotExist:
            cart_amount = 0
        if priced_product.stock_amount - cart_amount - amount < 0:
            # Заказывают больше, чем имеется
            result['error'] = 'Недостаточно товара для добавления в корзину'
            return JsonResponse(result)

    cart_products, created = CartProducts.objects.get_or_create(cart=cart,
                                                                priced_product=priced_product,
                                                                defaults={'amount': amount})
    if not created:
        cart_products.amount += amount
        cart_products.save()
    result['html'] = render_to_string('cart/cart_add_popover.html', {
        'amount': cart_products.amount,
        'priced_product': priced_product
    })
    return JsonResponse(result)


@require_POST
def remove_from_cart(request):
    priced_product = get_product(request)
    if priced_product is None:
        return HttpResponseBadRequest('Wrong parameters')

    # Корзина
    cart, created = get_cart(request)
    try:
        cart_product = CartProducts.objects.get(cart=cart,
                                                priced_product=priced_product)
    except CartProducts.DoesNotExist:
        return HttpResponseBadRequest('Not in cart')

    cart_product.delete()
    cart_items = CartProducts.objects_detailed.filter(cart=cart)
    result = {'html': render_to_string('cart/cart_form.html',
                                       {'cart': cart,
                                        'cart_items': cart_items,
                                        'cart_summary': cart.get_cart_summary(),
                                        'amount_template': 'cart/cart_amount.html'})}

    return JsonResponse(result)


@transaction.atomic
@require_POST
def update_cart(request):
    result = {}

    try:
        items = json.loads(request.POST['cart_items'])
    except (KeyError, ValueError):
        result['error'] = 'Неверные параметры'
        return JsonResponse(result)

    cart, created = get_cart(request)
    cart_items = []

    for item in items:
        try:
            cart_product = CartProducts.objects_detailed. \
                get(cart=cart, priced_product__id=item['product'])
            new_amount = int(item['amount'])
            if not new_amount == cart_product.stock_amount:
                # Количество товара не должно превысить количество на складе
                cart_product.amount = min(cart_product.stock_amount, new_amount)
                cart_product.save()
            cart_items.append(cart_product)
        except (CartProducts.DoesNotExist, KeyError, ValueError):
            result['error'] = 'Неверные параметры'
            return JsonResponse(result)

    result['html'] = render_to_string('cart/cart_form.html',
                                      {'cart': cart,
                                       'cart_items': cart_items,
                                       'cart_summary': cart.get_cart_summary(),
                                       'amount_template': 'cart/cart_amount.html'})

    return JsonResponse(result)


@require_GET
def get_cart_summary(request):
    cart, created = get_cart(request, False)
    result = {'html': render_to_string('cart/cart_widget.html', {'user_cart': cart})}
    return JsonResponse(result)


@require_POST
def update_checkout(request):
    cart, created = get_cart(request, False)
    user = get_user(request)

    # AJAX запрос на обновление формы
    checkout_form = CheckoutForm(cart, user, initial=request.POST)
    result = {
        'html': render_to_string('cart/checkout_form.html', {
            'form': checkout_form,
            'cart': cart,
            'cart_summary': checkout_form.cart_summary
        }, request=request)
    }
    return JsonResponse(result)


# Вьюхи


@require_http_methods(['GET', 'POST'])
def view_cart(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('cart:checkout'))

    if request.method == 'GET':
        cart, created = get_cart(request, False)
        cart_items = CartProducts.objects_detailed.filter(cart=cart). \
            select_related('priced_product__product__unit')
        return render(request, 'cart/cart.html', {
            'cart': cart,
            'cart_items': cart_items,
            'cart_summary': cart.get_cart_summary()
        })


@transaction.atomic
@require_http_methods(['GET', 'POST'])
def checkout(request):
    cart, created = get_cart(request, False)
    cart_items = CartProducts.objects.filter(cart=cart). \
        select_related('priced_product__product__unit')

    # Пустая корзина
    if not cart_items:
        return HttpResponseRedirect(reverse('cart:view'))

    user = get_user(request)

    if request.method == 'POST':

        checkout_form = CheckoutForm(cart, user, request.POST)
        if checkout_form.is_valid():
            # Если отмечено register, зарегистрировать пользователя
            if checkout_form.cleaned_data['register']:
                user, password = register_user(request,
                                               checkout_form.cleaned_data['email'])
                send_registration_email(user, password)

            # Записать заказ в базу по корзине
            order = create_new_order(checkout_form)

            # Очистить корзину
            cart.delete()

            # Перенаправление на страницу с заказом
            # Там же возможна дальнейшая оплата
            return HttpResponseRedirect(reverse('orders:direct_view', args=[order.uid]) + '?new_order')

        else:
            return render(request, 'cart/checkout.html', {
                'form': checkout_form,
                'cart': cart,
                'cart_items': cart_items,
                'cart_summary': checkout_form.cart_summary
            })

    if request.method == 'GET':

        initial = {}
        if initial_method:
            initial['shipment'] = initial_method.__name__
            initial['payment'] = initial_method.initial_gateway

        checkout_form = CheckoutForm(cart, user, initial=initial)
        return render(request, 'cart/checkout.html', {
            'form': checkout_form,
            'cart': cart,
            'cart_items': cart_items,
            'cart_summary': checkout_form.cart_summary
        })


# Вспомогательные функции


def get_product(request):
    try:
        return PricedProduct.objects_detailed.get(pk=int(request.POST['product_id']))
    except (KeyError, ValueError, PricedProduct.DoesNotExist):
        return None


def get_amount(request):
    try:
        return int(request.POST['amount'])
    except ValueError:
        return None
    except KeyError:
        return 1


def get_user(request):
    return request.user if request.user.is_authenticated() else None
