# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20150606_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(to='products.Product', verbose_name='Похожие товары'),
        ),
    ]
