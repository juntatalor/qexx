from django.db import models
from django.conf import settings

from products.models import Product, PricedProduct
from payment.models import Currency


# Модели


class Cart(models.Model):
    # Уникальный идентификатор сессии
    uid = models.CharField(verbose_name='Идентификатор', max_length=32)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', null=True)
    currency = models.ForeignKey(Currency, verbose_name='Валюта', default=Currency.get_main_currency_id)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def get_cart_summary(self):
        return CartProducts.objects.filter(cart=self).\
            aggregate(cart_price=models.Sum(models.F('amount') * models.F('priced_product__price')),
                      amount=models.Sum('amount'))


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='Корзина', related_name='cart_products')
    priced_product = models.ForeignKey(PricedProduct, verbose_name='Товар')
    amount = models.IntegerField(verbose_name='Количество')

    objects = models.Manager()
    objects_detailed = models.Manager()


def move_cart_to_session(old_session_key, new_session_key):
    try:
        cart = Cart.objects.get(uid=old_session_key)
    except Cart.DoesNotExist:
        # Не требуется миграция между сессиями - нет корзины в старой сессии
        return False
    cart.uid = new_session_key
    cart.save()
    return True