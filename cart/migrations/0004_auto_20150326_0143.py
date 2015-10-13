# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150325_0026'),
        ('cart', '0003_auto_20150324_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='products.PricedProduct', through='cart.CartProducts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='cart',
            field=models.ForeignKey(to='cart.Cart', verbose_name='Корзина'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=10, verbose_name='Сумма'),
            preserve_default=True,
        ),
    ]
