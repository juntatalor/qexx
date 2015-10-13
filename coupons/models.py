from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Category, Product
from payment.models import Currency
from orders.models import Order
from cart.models import Cart

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(verbose_name='Код купона', max_length=255, unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    date = models.DateTimeField(verbose_name='Дата начала действия', blank=True, null=True)
    expire_date = models.DateTimeField(verbose_name='Дата окончания действия', blank=True, null=True)
    currency = models.ForeignKey(Currency, verbose_name='Валюта', default=Currency.get_main_currency_id)
    max_usage = models.IntegerField(verbose_name='Максимальное количество использований', default=0)
    active = models.BooleanField(verbose_name='Активен', default=True)

    # Виды скидок
    discount_fix = models.DecimalField(verbose_name='Скидка (фиксированная)',
                                       decimal_places=2, max_digits=10, default=0)
    discount_percent = models.DecimalField(verbose_name='Скидка (процент)',
                                           decimal_places=2, max_digits=5, default=0,
                                           validators=[MaxValueValidator(100.00),
                                                       MinValueValidator(0.00)])
    discount_free_delivery = models.BooleanField(verbose_name='Бесплатная доставка', default=False)

    # В каких заказах использован купон
    orders = models.ManyToManyField(Order, blank=True)

    # В каких корзинах использован купон
    carts = models.ManyToManyField(Cart, blank=True)

    def __str__(self):
        discount_fix = '{0:.2f} {1}'.format(self.discount_fix, str(self.currency)) if self.discount_fix else ''
        discount_percent = '{0:.2f}%'.format(self.discount_percent) if self.discount_percent else ''
        discount_free_delivery = 'беспл. дост.' if self.discount_free_delivery else ''
        discount = [discount_fix, discount_percent, discount_free_delivery]
        return self.code + ' (' + ', '.join(x for x in discount if x) + ')'
