from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    short_name = models.CharField(verbose_name='Сокращение', max_length=255)
    is_main = models.BooleanField(verbose_name='Основная валюта', default=False)

    def get_exchange_rate(self, date):
        # Возвращает ближайший к date курс
        return self.exchange_rate.filter(date__lte=date).order_by('-date')[:1]

    @staticmethod
    def get_main_currency():
        try:
            return Currency.objects.get(is_main=True)
        except Currency.DoesNotExist:
            return None

    @staticmethod
    def get_main_currency_id():
        try:
            return Currency.objects.get(is_main=True).id
        except Currency.DoesNotExist:
            return None

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, verbose_name='Валюта', related_name='exchange_rate')
    rate = models.DecimalField(verbose_name='Курс', decimal_places=3, max_digits=10)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
