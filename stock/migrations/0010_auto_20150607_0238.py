# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_remove_comingproducts_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coming',
            name='products',
        ),
        migrations.AlterField(
            model_name='comingproducts',
            name='coming',
            field=models.ForeignKey(to='stock.Coming', related_name='coming_products', verbose_name='Поступление'),
        ),
    ]
