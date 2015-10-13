# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20150529_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', related_name='order_products', to='orders.Order'),
        ),
    ]
