from datetime import timedelta
from decimal import Decimal
import json

from django.test import TestCase, Client
from django.utils import timezone
from django.db.models import Count

from payment.models import Currency
from coupons.models import Coupon
from coupons.utils import coupon_valid, get_discount
from products.models import Unit, Category, Product, PricedProduct
from orders.models import Order, OrderProducts
from orders.constants import ORDER_STATUS, PAYMENT_STATUS
from shipping.models import Country
from cart.models import Cart, CartProducts

# Create your tests here.


class CouponTestCase(TestCase):

    def setUp(self):

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
                                     shipping_price=500,
                                     country=country)
        OrderProducts.objects.create(order=order, priced_product=priced_product, amount=60, price=200)

        cart = Cart.objects.create()
        CartProducts.objects.create(cart=cart, priced_product=priced_product, amount=50)

        # Неактивный купон
        Coupon.objects.create(code='cpn_inactive', active=False)
        # Купон с истекшей датой
        Coupon.objects.create(code='cpn_expire', expire_date=timezone.now() - timedelta(days=1))
        # Купон с неистекшей датой
        Coupon.objects.create(code='cpn_not_expire', expire_date=timezone.now() + timedelta(days=1))
        # Купон, еще не начавший действовать
        Coupon.objects.create(code='cpn_early', date=timezone.now() + timedelta(days=1))
        # Купон, начавший действовать
        Coupon.objects.create(code='cpn_not_early', date=timezone.now() - timedelta(days=1))
        # Купон, который использовался максимальное число раз
        cpn = Coupon.objects.create(code='cpn_used_max_times', max_usage=1)
        cpn.orders.add(order)
        # Купон, который не использовался максимальное число раз
        cpn = Coupon.objects.create(code='cpn_not_used_max_times', max_usage=2)
        cpn.orders.add(order)
        # Все ограничения в одном купоне + скидки
        cpn = Coupon.objects.create(code='cpn_all_valid',
                                    max_usage=5,
                                    expire_date=timezone.now() + timedelta(days=1),
                                    date=timezone.now() - timedelta(days=1),
                                    discount_fix=500.7,
                                    discount_percent=20,
                                    discount_free_delivery=True)
        cpn.orders.add(order)
        cpn.carts.add(cart)

    def test_coupon_valid(self):

        print('Тестирование функции coupon_valid')
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_inactive")), False)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_expire")), False)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_not_expire")), True)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_early")), False)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_not_early")), True)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_used_max_times")), False)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_not_used_max_times")), True)
        self.assertEqual(coupon_valid(Coupon.objects.get(code="cpn_all_valid")), True)

    def test_get_discount(self):

        print('Тестирование функций get_order_discount, get_cart_discount')
        order = Order.objects.get(pk=1)
        order_discount, free_delivery = get_discount(Coupon.objects.filter(orders=order),
                                                     order.get_order_summary()['price'])

        # Стоимость заказа 60 * 200 = 12000.00
        # - фиксированная скидка 500.7 = 11499.3
        # - скидка 20% = 11499.3 * 0.2 = 2299.86
        # - Общая скидка = 500.7 + 2299.86 = 2800.56
        self.assertEqual(order_discount, Decimal('2800.56'))
        self.assertEqual(free_delivery, True)

        cart = Cart.objects.get(pk=1)
        cart_discount, free_delivery = get_discount(Coupon.objects.filter(carts=cart),
                                                    cart.get_cart_summary()['cart_price'])

        # Стоимость корзины 50 * 100 = 5000
        # Фиксированная скидка 500.7 = 4499.3
        # Скидка 20% = 899.86
        # Общая скидка = 500.7 + 899.86 = 1400.56
        self.assertEqual(cart_discount, Decimal('1400.56'))
        self.assertEqual(free_delivery, True)

    def test_coupon_add(self):

        print('Тестирование coupons: /add_to_cart, /remove_from_cart, /get_coupons')
        c = Client()
        # Добавление корзины и купона в нее
        response = c.post('/coupons/add_to_cart/', {'coupon': 'cpn_all_valid'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content.decode('utf-8')))
        self.assertIn('html', data)
        self.assertNotIn('error', data)
        coupons_in_cart = Coupon.objects.filter(code='cpn_all_valid').aggregate(cnt=Count('carts'))
        self.assertEqual(coupons_in_cart['cnt'], 2)
        # Добавление в корзину несуществующего купона
        response = c.post('/coupons/add_to_cart/', {'coupon': 'some coupon code'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content.decode('utf-8')))
        self.assertIn('error', data)
        self.assertNotIn('html', data)
        # Проверка количества купонов в корзине
        coupons_in_cart = Coupon.objects.filter(code='cpn_all_valid').aggregate(cnt=Count('carts'))
        self.assertEqual(coupons_in_cart['cnt'], 2)
        # Удаление купона из корзины
        response = c.post('/coupons/remove_from_cart/', {'coupon': 'cpn_all_valid'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content.decode('utf-8')))
        self.assertIn('html', data)
        self.assertNotIn('error', data)
        # Проверка количества купонов в корзине
        coupons_in_cart = Coupon.objects.filter(code='cpn_all_valid').aggregate(cnt=Count('carts'))
        self.assertEqual(coupons_in_cart['cnt'], 1)