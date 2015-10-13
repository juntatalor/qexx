# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20150620_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='_main_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='images/product', verbose_name='Основное изображение', blank=True),
        ),
    ]
