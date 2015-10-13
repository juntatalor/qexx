# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_auto_20150514_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Дата начала действия'),
        ),
    ]
