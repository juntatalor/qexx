# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0005_auto_20150526_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]
