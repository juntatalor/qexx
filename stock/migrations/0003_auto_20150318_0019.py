# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stockrecord_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coming',
            name='comment',
            field=models.TextField(verbose_name='Коммментарий', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='comment',
            field=models.TextField(verbose_name='Коммментарий', blank=True),
            preserve_default=True,
        ),
    ]
