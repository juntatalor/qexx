# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20150504_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='cart',
            new_name='carts',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='products',
        ),
    ]
