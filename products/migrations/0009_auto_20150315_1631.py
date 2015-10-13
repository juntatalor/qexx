# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150315_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description_full',
            field=models.TextField(verbose_name='Расширенное описание', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=models.TextField(verbose_name='Короткое описание', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(verbose_name='Артикул', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
