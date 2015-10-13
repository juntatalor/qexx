# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150324_1946'),
        ('orders', '0006_auto_20150312_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproducts',
            name='variation_value',
            field=models.ForeignKey(blank=True, null=True, to='products.ProductVariationValue', verbose_name='Свойство'),
            preserve_default=True,
        ),
    ]
