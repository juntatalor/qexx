# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20150324_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comingproducts',
            name='variation_value',
        ),
        migrations.RemoveField(
            model_name='stockrecord',
            name='variation_value',
        ),
        migrations.AddField(
            model_name='comingproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Сумма', max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comingproducts',
            name='product',
            field=models.ForeignKey(to='products.PricedProduct', verbose_name='Товар'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='product',
            field=models.ForeignKey(to='products.PricedProduct', verbose_name='Продукт', related_name='stock_records'),
            preserve_default=True,
        ),
    ]
