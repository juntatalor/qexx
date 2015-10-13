# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150607_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='image',
            field=models.ImageField(blank=True, verbose_name='Изображение', upload_to='images/rating'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='moderated',
            field=models.BooleanField(verbose_name='Модерация пройдена', default=False),
        ),
    ]
