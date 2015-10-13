# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_orderproducts_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(default=0, verbose_name='Стоимость доставки', max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
