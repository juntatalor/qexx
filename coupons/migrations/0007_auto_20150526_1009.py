# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0006_auto_20150526_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='carts',
            field=models.ManyToManyField(to='cart.Cart', blank=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='orders',
            field=models.ManyToManyField(to='orders.Order', blank=True),
        ),
    ]
