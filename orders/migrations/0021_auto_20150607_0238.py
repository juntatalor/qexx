# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20150607_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(to='orders.Order', related_name='order_products', verbose_name='Заказ'),
        ),
    ]
