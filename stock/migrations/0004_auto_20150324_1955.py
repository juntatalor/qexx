# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150324_1946'),
        ('stock', '0003_auto_20150318_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='comingproducts',
            name='variation_value',
            field=models.ForeignKey(blank=True, null=True, to='products.ProductVariationValue', verbose_name='Свойство'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='variation_value',
            field=models.ForeignKey(blank=True, null=True, to='products.ProductVariationValue', verbose_name='Свойство'),
            preserve_default=True,
        ),
    ]
