# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('products', '0012_productprice_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('default', models.BooleanField(verbose_name='Свойство по уомлчанию', default=False)),
                ('price', models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)),
                ('currency', models.ForeignKey(verbose_name='Валюта', default=payment.models.Currency.get_main_currency_id, to='payment.Currency')),
                ('product', models.ForeignKey(verbose_name='Товар', to='products.Product', related_name='prices')),
                ('variation_value', models.ForeignKey(verbose_name='Свойство', null=True, to='products.ProductVariationValue', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='variation_value',
        ),
        migrations.DeleteModel(
            name='ProductPrice',
        ),
    ]
