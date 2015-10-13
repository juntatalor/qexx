# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_unit'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockrecord',
            name='product',
            field=models.ForeignKey(default=1, to='products.Product', related_name='stock_records', verbose_name='Продукт'),
            preserve_default=False,
        ),
    ]
