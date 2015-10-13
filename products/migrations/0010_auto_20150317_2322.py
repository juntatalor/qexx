# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20150315_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(verbose_name='Изображение', blank=True, upload_to='images/category'),
            preserve_default=True,
        ),
    ]
