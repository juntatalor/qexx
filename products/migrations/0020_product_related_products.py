# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20150526_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ForeignKey(default=0, verbose_name='Похожие товары', to='products.Product'),
            preserve_default=False,
        ),
    ]
