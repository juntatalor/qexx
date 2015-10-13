__author__ = 'Сергей'

from django.db import models
from django.contrib.sites.models import Site


class DetailedSite(models.Model):
    site = models.OneToOneField(Site, verbose_name='Сайт')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    address = models.TextField(verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.site)