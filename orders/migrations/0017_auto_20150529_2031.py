# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20150529_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_price',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Стоимость доставки', max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='staff_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий персонала'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий покупателя'),
        ),
    ]
