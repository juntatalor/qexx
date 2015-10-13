# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='Код купона')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateField(blank=True, verbose_name='Дата начала действия', null=True)),
                ('expire_date', models.DateTimeField(blank=True, verbose_name='Дата окончания действия', null=True)),
                ('max_usage', models.IntegerField(default=0, verbose_name='Максимальное количество использований')),
                ('active', models.BooleanField(default=True, verbose_name='Активен')),
                ('discount_fix', models.DecimalField(default=0, decimal_places=2, verbose_name='Скидка (фиксированная)', max_digits=10)),
                ('discount_percent', models.DecimalField(default=0, decimal_places=2, verbose_name='Скидка (процент)', max_digits=5)),
                ('discount_free_delivery', models.BooleanField(default=False, verbose_name='Бесплатная доставка')),
                ('categories', models.ManyToManyField(to='products.Category')),
                ('currency', models.ForeignKey(to='payment.Currency', null=True, blank=True, verbose_name='Валюта')),
                ('orders', models.ManyToManyField(to='orders.Order')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
