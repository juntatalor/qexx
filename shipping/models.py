from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    full_name = models.CharField(verbose_name='Полное наименование', max_length=255)
    is_main = models.BooleanField(verbose_name='Основная страна', default=False)
    code = models.CharField(verbose_name='Код', max_length=3)
    code_a2 = models.CharField(verbose_name='Код альфа-2', max_length=2)
    code_a3 = models.CharField(verbose_name='Код альфа-3', max_length=3)

    def __str__(self):
        return self.name.title()

    @staticmethod
    def default_country():
        try:
            return Country.objects.get(is_main=True)
        except Country.DoesNotExist:
            return None

    @staticmethod
    def default_country_id():
        try:
            return Country.objects.get(is_main=True).id
        except Country.DoesNotExist:
            return None

    class Meta:
        ordering = ['name']