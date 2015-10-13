# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_packageproduct'),
        ('stock', '0011_stockorderproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockorderproducts',
            name='priced_product',
            field=models.ForeignKey(verbose_name='Товар', default=0, to='products.PricedProduct'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stockorderproducts',
            name='order_product',
            field=models.ForeignKey(related_name='stock_order_products', to='orders.OrderProducts'),
        ),
    ]
