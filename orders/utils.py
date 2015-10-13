__author__ = 'Сергей'

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from orders.models import Order
from shipping.methods import methods
from payment.gateways import gateways


def send_new_order_email(email, order):
    """
    Посылает почту пользователю, оформившему заказ
    Используется шаблон
    :param email:
    :param order:
    :return:
    """
    send_mail('Заказ № %s в магазине %s' % (order.id, get_current_site(None).domain),
              render_to_string('orders/email/new_order.html', {'order': order}),
              settings.EMAIL_REPLY,
              [email, ],
              fail_silently=True
              )


def create_new_order(checkout_form):
    """
    Создает новый заказ, используя информацию о форме чекаута, корзине и пользователе
    :param checkout_form:
    :param cart:
    :param user:
    :return:
    """
    data = checkout_form.cleaned_data
    cart_summary = checkout_form.cart_summary

    shipping_method = methods[data['shipment']](cart=checkout_form.cart)
    payment_method = gateways[data['payment']]()
    order = Order(cart=checkout_form.cart,
                  user=checkout_form.user,
                  shipping_method=data['shipment'],
                  payment_method=data['payment'],
                  order_status=shipping_method.order_status,
                  payment_status=payment_method.payment_status,
                  shipping_price=cart_summary['shipping_price'],
                  shipping_address=data.get('address', ''),
                  phone=data.get('phone', ''),
                  email=data['email'],
                  contact_person=data['first_name'] + ' ' + data['last_name'],
                  discount=cart_summary['discount']
                  )
    order.save()

    # Сформировать и отправить письмо с заказом
    send_new_order_email(data['email'], order)

    # ToDo Письмо администраторам

    return order
