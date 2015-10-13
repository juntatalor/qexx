# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderproducts_variation_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproducts',
            name='variation_value',
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Сумма', max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='product',
            field=models.ForeignKey(to='products.PricedProduct', verbose_name='Товар'),
            preserve_default=True,
        ),
    ]
