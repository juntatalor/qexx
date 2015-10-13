# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_auto_20150516_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0)], default=0, max_digits=5, verbose_name='Скидка (процент)'),
        ),
    ]
