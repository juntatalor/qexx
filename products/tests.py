from django.test import TestCase

from products.models import Category, Product, Unit

# Create your tests here.


class ProductTestCase(TestCase):
    def setUp(self):
        print('Загрузка тестовых данных ProductTestCase')
        # Единица измерения
        Unit.objects.create(name='шт.')

    def test_slug(self):
        # Тестирование класса AutoSlugField
        print('Тестирование создания slug')
        cat = Category.objects.create(name='Тестовая категория')
        self.assertEqual(cat.slug, 'testovaia-kategoriia')
        product = Product.objects.create(name='Очень хороший продукт', unit=Unit.objects.get(name='шт.'))
        self.assertEqual(product.slug, 'ochen-khoroshii-produkt')
        product = Product.objects.create(name='Очень хороший продукт', unit=Unit.objects.get(name='шт.'))
        self.assertEqual(product.slug, 'ochen-khoroshii-produkt-2')