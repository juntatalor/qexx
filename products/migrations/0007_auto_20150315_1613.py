# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150215_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_full',
            field=models.TextField(default='', verbose_name='Расширенное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=models.TextField(verbose_name='Короткое описание'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='low_balance',
            field=models.IntegerField(default=0, verbose_name='Низкий остаток'),
            preserve_default=True,
        ),
    ]
