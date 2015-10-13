# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150324_1946'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproducts',
            name='product',
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='priced_product',
            field=models.ForeignKey(to='products.PricedProduct', default=0, verbose_name='Товар'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='cart',
            field=models.ForeignKey(related_name='cart_products', to='cart.Cart', verbose_name='Корзина'),
            preserve_default=True,
        ),
    ]
