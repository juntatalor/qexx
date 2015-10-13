from django.db import models
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from autoslug import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField

from payment.models import Currency

MISSING_IMAGE_PATH = 'no_photo.png'

# Модели


class Unit(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(verbose_name='Название категории', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=255)
    parent = TreeForeignKey('self', verbose_name='Родитель', null=True, blank=True, related_name='children')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/category', blank=True)

    def get_children_fk(self):

        """
        Получает количество продуктов в дочерних категориях.
        При этом учитывается полное прохождение дерева "вниз"
        Не учитываются продукты без цены
        """

        q = self.get_descendants(). \
            annotate(models.Count('product'),
                     min_price=models.Min('product__prices__price')). \
            filter(min_price__isnull=False). \
            values()
        res = []
        count = -1
        for item in q:
            if item['level'] == self.level + 1:
                res.append(item)
                count += 1
            else:
                res[count]['product__count'] += item['product__count']
        return res

    def __str__(self):
        return self.name


class DetailedProductManager(models.Manager):
    def get_queryset(self):
        """
        Возвращает товары, для которых указана цена в основной валюте
        Получает минимальную и максимальную цены на товар
        :return:
        """
        qs = super(DetailedProductManager, self).get_queryset(). \
            filter(prices__currency=Currency.get_main_currency()). \
            annotate(min_price=models.Min('prices__price'),
                     max_price=models.Max('prices__price')). \
            prefetch_related('prices')

        return qs


class Product(models.Model):
    # Статусы показа остатков

    STOCK_DO_NOT_SHOW = -1
    STOCK_AVAILABLE = 0
    STOCK_EXACT = 1
    STOCK_LOW_BALANCE = 2

    STOCK_CHOICES = (
        (STOCK_DO_NOT_SHOW, 'Не показывать остаток'),
        (STOCK_AVAILABLE, 'Всегда доступно'),
        (STOCK_EXACT, 'Показывать точный остаток'),
        (STOCK_LOW_BALANCE, 'Показывать остаток, когда товар заканчивается'),
    )  # Статус продукта

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Черновик'),
        (STATUS_PUBLISHED, 'Опубликован'),
    )

    TYPE_COMMON = 0
    TYPE_VARIATIVE = 1

    TYPE_CHOICES = (
        (TYPE_COMMON, 'Обычный продукт'),
        (TYPE_VARIATIVE, 'Вариативный продукт')
    )

    name = models.CharField(verbose_name='Название товара', max_length=255)
    description_short = models.TextField(verbose_name='Короткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    description_full = models.TextField(verbose_name='Расширенное описание', blank=True)

    slug = AutoSlugField(populate_from='name', unique=True, max_length=255)
    sku = models.CharField(verbose_name='Артикул', max_length=255, blank=True)
    type = models.IntegerField(verbose_name='Тип продукта',
                               choices=TYPE_CHOICES, default=TYPE_COMMON)
    low_balance = models.IntegerField(verbose_name='Низкий остаток', default=0)
    stock_track = models.IntegerField(verbose_name='Метод отображения остатков',
                                      choices=STOCK_CHOICES, default=STOCK_DO_NOT_SHOW)
    status = models.IntegerField(verbose_name='Статус',
                                 choices=STATUS_CHOICES, default=STATUS_DRAFT)
    unit = models.ForeignKey(Unit, verbose_name='Единица измерения')
    popular = models.BooleanField(verbose_name='Популярный товар')

    _main_image = ThumbnailerImageField(upload_to='images/product', blank=True, verbose_name='Основное изображение')

    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    categories = TreeManyToManyField(Category, verbose_name='Категории')
    # ToDo: вообще, конечно, symmetrical=True это круто для похожих товаров, но на период тестирования отключим, мешает
    related_products = models.ManyToManyField('self', symmetrical=False, verbose_name='Похожие товары')

    objects = models.Manager()
    objects_detailed = DetailedProductManager()

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def get_price_range(self):
        # Возвращает минимальную и максимальную цены на вариации товара
        currency = Currency.get_main_currency()
        res = PricedProduct.objects.filter(product=self,
                                           currency=currency). \
            aggregate(min_price=models.Min('price'),
                      max_price=models.Max('price'))

        res['currency'] = currency
        return res

    @property
    def main_image(self):
        return self._main_image or MISSING_IMAGE_PATH

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', verbose_name='Изображения')
    path = ThumbnailerImageField(upload_to='images/product')
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.path)


class ProductVariation(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)

    def __str__(self):
        return self.name


class ProductVariationValue(models.Model):
    variation = models.ForeignKey(ProductVariation, verbose_name='Тип свойства')
    name = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return str(self.variation) + ': ' + self.name

    class Meta:
        ordering = ['variation__name', 'name']


class PricedProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='prices')
    currency = models.ForeignKey(Currency, verbose_name='Валюта', default=Currency.get_main_currency_id)
    variation_value = models.ForeignKey(ProductVariationValue, verbose_name='Свойство', null=True, blank=True)
    default = models.BooleanField(verbose_name='Свойство по умолчанию', default=False)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)
    status = models.IntegerField(verbose_name='Статус',
                                 choices=Product.STATUS_CHOICES, default=Product.STATUS_DRAFT)
    # Используется если не подключен склад
    # amount = models.IntegerField(verbose_name='Количество')

    objects = models.Manager()
    objects_detailed = models.Manager()

    def __str__(self):
        if self.variation_value:
            return str(self.product) + " (" + str(self.variation_value) + ")"
        else:
            return str(self.product)


class PackageProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='package')
    additional_product = models.ForeignKey(PricedProduct, verbose_name='Товар для списания')
    distribute_amount = models.IntegerField(verbose_name='Количество')
