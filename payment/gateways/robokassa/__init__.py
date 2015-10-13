__author__ = 'Сергей'

from hashlib import md5

from django.conf.urls import patterns, url
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from payment.gateways import BaseGateway
from orders.constants import PAYMENT_STATUS
from orders.models import Order


def check_crc(request):
    if request.method == Robokassa.method:
        values = getattr(request, Robokassa.method)
        out_summ = getattr(values, 'nOutSum', None)
        inv_id = getattr(values, 'nInvId', None)
        crc = getattr(values, 'sSignatureValue', None)

        if None in [out_summ, inv_id, crc]:
            return False

        _my_crc = out_summ + inv_id + Robokassa.mrch_pass2
        my_crc = md5(_my_crc.encode('utf-8')).hexdigest()
        if not my_crc == crc:
            # Ошибка проверки контрольной суммы
            return False
        # Проверки пройдены
        return inv_id
    # Неверный метод
    return False


@require_http_methods(['GET', 'POST'])
def result_view(request):
    """
    Вьюха, отвечающая на запрос Result Робокассы
    :param request:
    :return:
    """
    inv_id = check_crc(request)
    if not inv_id:
        return HttpResponseBadRequest('Wrong parameters')

    try:
        order_id = int(inv_id)
        order = Order.objects.get(pk=order_id)
    except (ValueError, Order.DoesNotExist):
        return HttpResponseBadRequest('Wrong parameters')

    order.payment_status = PAYMENT_STATUS['PAYED']
    order.save()
    # ToDo: отослать письмо об упешной оплате заказа
    return HttpResponse('OK' + inv_id)


@require_http_methods(['GET', 'POST'])
def success_view(request):
    """
    Вьюха, отвечабющая на запрос Success Робокассы
    :param request:
    :return:
    """
    inv_id = check_crc(request)
    if not inv_id:
        return HttpResponseBadRequest('Wrong parameters')

    try:
        order_id = int(inv_id)
        order = Order.objects.get(pk=order_id)
    except (ValueError, Order.DoesNotExist):
        return HttpResponseBadRequest('Wrong parameters')

    # ToDo: здесь неплохо бы проверять, что уже был вызван result_url (order.payment_status == PAYMENT_STATUS['PAYED'])
    return render(request, 'payment/success.html', {'order': order})


@require_http_methods(['GET', 'POST'])
def fail_view(request):
    """
    Вьюха, отвечабющая на запрос Fail Робокассы
    :param request:
    :return:
    """

    return render(request, 'payment/fail.html')


class Robokassa(BaseGateway):
    """
    Шлюз для оплаты с помощью Robokassa.ru
    """
    id = 'Robokassa'
    name = 'Robokassa'
    help_text = 'Оплата с помощью <a href="http://robokassa.ru">Робокассы</a>'
    online_payment = True
    urls = patterns('',
                    url(r'^robokassa/result$', result_view),
                    url(r'^robokassa/success$', success_view),
                    url(r'^robokassa/fail$', fail_view),
                    )

    # Данные Робокассы
    mrch_login = 'ardushop'
    mrch_pass1 = 'passwordnumber1here'
    mrch_pass2 = 'passwordnumber2here'
    # Пока что будем использовать один метод.
    # Вообще робокасса для каждого урла позволяет назначить свой метод
    method = 'GET'

    @classmethod
    def get_payment_url(cls, order):
        # Описание тут: http://www.robokassa.ru/ru/Doc/Ru/Interface.aspx
        out_summ = str(order.get_order_summary()['price'])
        inv_id = str(order.pk)
        crc = cls.mrch_login + out_summ + inv_id + cls.mrch_pass1
        crc = md5(crc.encode('utf-8')).hexdigest()
        return 'https://auth.robokassa.ru/Merchant/Index.aspx?' \
               'MrchLogin=%s&OutSum=%s&InvId=%s&SignatureValue=%s' % (
                   cls.mrch_login, out_summ, inv_id, crc
               )


GATEWAY = Robokassa
