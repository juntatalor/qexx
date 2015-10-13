# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_related_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_products',
        ),
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(to='products.Product', related_name='related_products_rel_+', verbose_name='Похожие товары'),
        ),
    ]
