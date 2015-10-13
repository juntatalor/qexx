# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150325_0026'),
        ('orders', '0009_auto_20150326_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='products.PricedProduct', through='orders.OrderProducts'),
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', to='orders.Order'),
        ),
    ]
