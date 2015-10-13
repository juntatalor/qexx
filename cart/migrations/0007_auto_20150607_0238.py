# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_cartproducts_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='cart',
            field=models.ForeignKey(to='cart.Cart', related_name='cart_products', verbose_name='Корзина'),
        ),
    ]
