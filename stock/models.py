from django.db import models
from django.db.models import Sum, F, Q, Case, When, Value
from django.db.models.functions import Coalesce

from products.models import PricedProduct, Product, DetailedProductManager
from payment.models import Currency
from orders.models import OrderProducts
from cart.models import CartProducts

# Обновление бизнес-логики


class StockProductManager(DetailedProductManager):
    def get_queryset(self):
        return super(StockProductManager, self).get_queryset(). \
            annotate(stock_amount=Sum(
            Case(
                When(Q(prices__comingproducts__id__isnull=True) |
                     Q(prices__comingproducts__coming__received=False),
                     then=Value(0)),
                default='prices__comingproducts__amount',
                output_field=models.IntegerField())) - Coalesce(Sum('prices__stockrecord__amount'), 0))


class StockPricedProductManager(models.Manager):
    def get_queryset(self):
        return super(StockPricedProductManager, self).get_queryset(). \
            annotate(stock_amount=models.Sum(
            models.Case(
                models.When(models.Q(comingproducts__id__isnull=True) |
                            models.Q(comingproducts__coming__received=False),
                            then=models.Value(0)),
                default='comingproducts__amount',
                output_field=models.IntegerField()))
                                  - Coalesce(models.Sum('stockrecord__amount'), 0))


class StockCartProductsManager(models.Manager):
    def get_queryset(self):
        return super(StockCartProductsManager, self).get_queryset(). \
            annotate(stock_amount=Sum(
            Case(
                When(Q(priced_product__comingproducts__id__isnull=True) |
                     Q(priced_product__comingproducts__coming__received=False),
                     then=Value(0)),
                default='priced_product__comingproducts__amount',
                output_field=models.IntegerField()))
                                  - Coalesce(Sum('priced_product__stockrecord__amount'), 0))


def set_detailed_manager(model, manager):
    # ToDo: непонятно, насколько хорош такой подход. Нужны тесты.
    new_manager = manager()
    new_manager.model = model
    model.objects_detailed = new_manager


set_detailed_manager(Product, StockProductManager)
set_detailed_manager(PricedProduct, StockPricedProductManager)
set_detailed_manager(CartProducts, StockCartProductsManager)

# Модели


class Supplier(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    link = models.CharField(verbose_name='Ссылка в интернете', max_length=255)
    comment = models.TextField(verbose_name='Коммментарий', blank=True)

    def __str__(self):
        return self.name


class Coming(models.Model):
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', null=True, blank=True)
    currency = models.ForeignKey(Currency, verbose_name='Валюта', default=Currency.get_main_currency_id)
    date_ordered = models.DateTimeField(verbose_name='Дата заказа', blank=True, null=True)
    date_shipped = models.DateTimeField(verbose_name='Дата отправки', blank=True, null=True)
    date_received = models.DateTimeField(verbose_name='Дата получения', blank=True, null=True)
    received = models.BooleanField(verbose_name='Получен', default=False)
    comment = models.TextField(verbose_name='Коммментарий', blank=True)

    def __str__(self):
        return 'Поступление %d от %s' % (self.id, self.supplier)

    def get_coming_summary(self):
        # Получает суммарную стоимость поступления
        return ComingProducts.objects.filter(coming=self). \
            aggregate(price=Sum(F('amount') * F('priced_poduct__price')),
                      amount=Sum('amount'))


class ComingProducts(models.Model):
    coming = models.ForeignKey(Coming, verbose_name='Поступление', related_name='coming_products')
    priced_product = models.ForeignKey(PricedProduct, verbose_name='Товар')
    amount = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)


class StockRecord(models.Model):
    # Таблица для соединения ComingProducts и OrderProducts в разрезе количественного учета
    # Указывает, какие конкретно из поступивших товаров были проданы

    # Поля для организации учета по партиям
    priced_product = models.ForeignKey(PricedProduct, verbose_name='Продукт')
    coming_products = models.ForeignKey(ComingProducts, verbose_name='Партия')
    order_products = models.ForeignKey(OrderProducts, verbose_name='Заказ')

    # Количество товаров, списанное с партии
    amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        # ToDo: product.unit вместо шт
        return 'Списание ' + str(self.priced_product) + ' ' + str(self.amount) + ' шт.'


class StockOrderProducts(models.Model):
    # Расширение для модели OrderProducts для хранения уже списанного товара
    order_products = models.ForeignKey(OrderProducts, related_name='stock_order_products')
    priced_product = models.ForeignKey(PricedProduct, verbose_name='Товар')
    distributed_amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        # ToDo: product.unit вместо шт
        return 'Списано ' + str(self.priced_product) + ' ' + str(self.distributed_amount) + ' шт.'
