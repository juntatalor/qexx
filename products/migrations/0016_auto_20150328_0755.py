# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150325_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.IntegerField(verbose_name='Тип продукта', default=0, choices=[(0, 'Обычный продукт'), (1, 'Вариативный продукт')]),
        ),
        migrations.AlterField(
            model_name='pricedproduct',
            name='default',
            field=models.BooleanField(verbose_name='Свойство по уомолчанию', default=False),
        ),
    ]
