# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20150324_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=10, verbose_name='Сумма'),
            preserve_default=True,
        ),
    ]
