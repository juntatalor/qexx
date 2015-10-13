# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_cartproducts_total'),
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='cart',
            field=models.ManyToManyField(to='cart.Cart'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='currency',
            field=models.ForeignKey(to='payment.Currency', default=payment.models.Currency.get_main_currency_id, verbose_name='Валюта'),
        ),
    ]
