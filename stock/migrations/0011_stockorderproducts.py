# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20150607_0238'),
        ('stock', '0010_auto_20150607_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockOrderProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('distributed_amount', models.IntegerField(verbose_name='Количество')),
                ('order_product', models.OneToOneField(to='orders.OrderProducts')),
            ],
        ),
    ]
