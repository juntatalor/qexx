from django.test import TestCase
from django.test import Client

from payment.models import Currency
from products.models import Category, Product, Unit, PricedProduct
from cart.models import Cart, CartProducts
from stock.models import Coming, Supplier, ComingProducts

# Тесты для приложения cart


class CartTestCase(TestCase):
    def setUp(self):
        print('Загрузка тестовых данных CartTestCase')
        # Создание основной валюты, единицы измерения
        Currency.objects.create(name='RUB', is_main=True)
        unit = Unit.objects.create(name='шт.')

        # Создание категории и продукта в этой категории
        category = Category.objects.create(name='Тестовая категория')
        product = Product.objects.create(name='Тестовый продукт', unit=unit)
        product.categories.add(category)
        priced_product = PricedProduct.objects.create(product=product, price=100)

        # Создание тестового поставщика и поступления
        supplier = Supplier.objects.create(name='Тестовый поставщик')

        # Создадим поступление для продукта
        coming = Coming.objects.create(supplier=supplier, received=True)
        ComingProducts.objects.create(coming=coming, priced_product=priced_product, amount=5, price=500)

    def check_cart(self, cart_amount, cart_products_amount, product_id=None, product_amount=None):
        self.assertEqual(len(Cart.objects.all()), cart_amount)
        self.assertEqual(len(CartProducts.objects.all()), cart_products_amount)
        if cart_products_amount > 0:
            self.assertEqual(CartProducts.objects.all()[0].priced_product.id, product_id)
            self.assertEqual(CartProducts.objects.all()[0].amount, product_amount)

    def test_ajax_cart(self):
        print('Тестирование /cart/add, /cart/remove')
        c = Client()
        # Добавление товара, 4 шт
        response = c.post('/cart/add/', {'product_id': 1,
                                         'amount': 4})
        self.assertEqual(response.status_code, 200)
        # Проверка корзины
        self.check_cart(1, 1, 1, 4)

        # Добавление товара, еще 1 шт
        response = c.post('/cart/add/', {'product_id': 1})
        self.assertEqual(response.status_code, 200)
        # Проверка корзины
        self.check_cart(1, 1, 1, 5)

        # Добавление товара, еще 1 шт - нельзя, больше нет в наличии
        # ToDo: нужно поправить этот тест
        # response = c.post('/cart/add/', {'product_id': 1})
        # self.assertEqual(response.status_code, 400)

        # Удаление товара
        response = c.post('/cart/remove/', {'product_id': 1})
        self.assertEqual(response.status_code, 200)
        # Проверка корзины
        self.check_cart(1, 0)

        # Добавление несуществующего товара
        response = c.post('/cart/add/', {'product_id': 2})
        self.assertEqual(response.status_code, 400)
        # Добавление без параметров
        response = c.post('/cart/add/')
        self.assertEqual(response.status_code, 400)

        # ToDo: cart/update