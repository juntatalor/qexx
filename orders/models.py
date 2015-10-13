from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

from products.models import PricedProduct
from payment.models import Currency
from orders.constants import ORDER_STATUS_CHOICES, ORDER_PAYMENT_STATUS_CHOICES
from orders.signals import order_post_save
from cart.models import CartProducts
from shipping.models import Country


class Order(models.Model):

    uid = models.CharField(verbose_name='Идентификатор', max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', null=True)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    order_status = models.IntegerField(verbose_name='Статус заказа', choices=ORDER_STATUS_CHOICES)
    payment_status = models.IntegerField(verbose_name='Статус оплаты', choices=ORDER_PAYMENT_STATUS_CHOICES)
    currency = models.ForeignKey(Currency, verbose_name='Валюта', default=Currency.get_main_currency_id)
    payment_method = models.CharField(verbose_name='Метод оплаты', max_length=255)
    shipping_method = models.CharField(verbose_name='Метод доставки', max_length=255)
    country = models.ForeignKey(Country, verbose_name='Страна', default=Country.default_country_id)
    shipping_address = models.TextField(verbose_name='Адрес', blank=True)
    shipping_price = models.DecimalField(verbose_name='Стоимость доставки', decimal_places=2, max_digits=10, default=0)
    phone = models.CharField(verbose_name='Телефон', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=255)
    contact_person = models.CharField(verbose_name='Контактное лицо', max_length=255)
    discount = models.DecimalField(verbose_name='Скидка', decimal_places=2, max_digits=10, default=0)

    user_comment = models.TextField(verbose_name='Комментарий покупателя', blank=True)
    staff_comment = models.TextField(verbose_name='Комментарий персонала', blank=True)

    def get_order_summary(self):
        return OrderProducts.objects.filter(order=self).\
            aggregate(price=models.Sum(models.F('amount') * models.F('price')),
                      amount=models.Sum('amount'))

    def get_total_price(self):
        return self.get_order_summary()['price'] + self.shipping_price - self.discount

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # Создание идентификатора для новых заказов
        if not self.id:
            self.uid = get_random_string(20)
        super(Order, self).save(force_insert, force_update, using,
                                update_fields)
        # Заполнение товаров
        if self.cart:
            cart_items = CartProducts.objects.filter(cart=self.cart).\
                select_related('priced_product')
            for item in cart_items:
                OrderProducts.objects.create(order=self,
                                             priced_product=item.priced_product,
                                             amount=item.amount,
                                             price=item.priced_product.price)
        # Обычный post_save не подходит, т.к. вызывается в super().save раньше, чем будут заполнены товары
        order_post_save.send(sender=self.__class__, instance=self)

    def __str__(self):
        return 'Заказ №' + str(self.id) + ' от ' + self.date.strftime('%x')

    def __init__(self, *args, **kwargs):
        # Корзина, которая будет использоваться для оформления заказа
        self.cart = kwargs.pop('cart', None)
        super(Order, self).__init__(*args, **kwargs)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='order_products')
    priced_product = models.ForeignKey(PricedProduct, verbose_name='Товар')
    amount = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)