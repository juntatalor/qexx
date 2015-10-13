# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20150607_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', to='orders.Order'),
        ),
    ]
