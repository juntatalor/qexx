from django.test import TestCase

# Create your tests here.

from django.utils import timezone
from stock.models import Supplier, Coming, StockRecord, ComingProducts
from stock.utils import create_sr_main
from stock.constants import LIFO, FIFO
from orders.models import Order, OrderProducts
from orders.constants import ORDER_STATUS, PAYMENT_STATUS
from products.models import Product, Category, Unit, PricedProduct
from payment.models import Currency
from shipping.models import Country


class ProductTestCase(TestCase):
    def setUp(self):

        print('Загрузка тестовых данных ProductTestCase')

        # Создание основной валюты, единицы измерения, страны
        Currency.objects.create(name='RUB', is_main=True)
        unit = Unit.objects.create(name='шт.')
        country = Country.objects.create(name='Тестовая страна')

        # Создание категории и продукта в этой категории
        category = Category.objects.create(name='Тестовая категория')
        product = Product.objects.create(name='Тестовый продукт', unit=unit)
        product.categories.add(category)
        priced_product = PricedProduct.objects.create(product=product, price=100)

        # Создание тестового заказа
        order = Order.objects.create(order_status=ORDER_STATUS['RECEIVED'],
                                     payment_status=PAYMENT_STATUS['NOT_PAYED'],
                                     shipping_price=0,
                                     country=country)
        OrderProducts.objects.create(order=order, priced_product=priced_product, amount=60, price=200)

        # Создание тестового поставщика и поступлений
        supplier = Supplier.objects.create(name='Тестовый поставщик')
        coming = Coming.objects.create(supplier=supplier, date_received=timezone.now(), received=True)
        ComingProducts.objects.create(coming=coming, priced_product=priced_product, amount=50, price=100)
        coming = Coming.objects.create(supplier=supplier, date_received=timezone.now(), received=True)
        ComingProducts.objects.create(coming=coming, priced_product=priced_product, amount=30, price=100)

    def test_create_stock_records_FIFO(self):
        # Тестирование stock.models.create_stock_records
        print('Тестирование складских списаний - FIFO')
        order = Order.objects.get(pk=1)
        create_sr_main(order, FIFO)
        # Списания, которые должны были произойти:
        # FIFO, списание coming(pk=1) - 50, списание coming(pk=2) - 10
        stock_records = StockRecord.objects.all()

        self.assertEqual(len(stock_records), 2)
        self.assertEqual(stock_records[0].amount, 50)
        self.assertEqual(stock_records[0].coming_products.id, 1)
        self.assertEqual(stock_records[1].amount, 10)
        self.assertEqual(stock_records[1].coming_products.id, 2)

    def test_create_stock_records_LIFO(self):
        # Тестирование stock.models.create_stock_records
        print('Тестирование складских списаний - LIFO')
        order = Order.objects.get(pk=1)
        create_sr_main(order, LIFO)
        # Списания, которые должны были произойти:
        # FIFO, списание coming(pk=2) - 30, списание coming(pk=1) - 30
        stock_records = StockRecord.objects.all()

        self.assertEqual(len(stock_records), 2)
        self.assertEqual(stock_records[0].amount, 30)
        self.assertEqual(stock_records[0].coming_products.id, 2)
        self.assertEqual(stock_records[1].amount, 30)
        self.assertEqual(stock_records[1].coming_products.id, 1)