# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150325_0026'),
        ('stock', '0005_auto_20150324_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='coming',
            name='products',
            field=models.ManyToManyField(to='products.PricedProduct', through='stock.ComingProducts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coming',
            name='received',
            field=models.BooleanField(default=False, verbose_name='Получен'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comingproducts',
            name='coming',
            field=models.ForeignKey(to='stock.Coming', verbose_name='Поступление'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comingproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=10, verbose_name='Сумма'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='product',
            field=models.ForeignKey(to='products.PricedProduct', verbose_name='Продукт'),
            preserve_default=True,
        ),
    ]
