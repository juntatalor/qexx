# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20150529_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Скидка'),
        ),
    ]
