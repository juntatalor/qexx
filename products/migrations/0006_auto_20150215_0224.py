# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=mptt.fields.TreeManyToManyField(verbose_name='Категории', to='products.Category'),
            preserve_default=True,
        ),
    ]
