# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20150607_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(blank=True, verbose_name='Адрес'),
        ),
    ]
