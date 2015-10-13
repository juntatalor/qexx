# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('payment', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_ordered', models.DateTimeField(blank=True, verbose_name='Дата заказа', null=True)),
                ('date_shipped', models.DateTimeField(blank=True, verbose_name='Дата отправки', null=True)),
                ('date_received', models.DateTimeField(blank=True, verbose_name='Дата получения', null=True)),
                ('comment', models.TextField(verbose_name='Коммментарий')),
                ('currency', models.ForeignKey(to='payment.Currency',
                                               default=payment.models.Currency.get_main_currency_id,
                                               verbose_name='Валюта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComingProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Цена', max_digits=10)),
                ('coming', models.ForeignKey(related_name='coming_products', to='stock.Coming', verbose_name='Поступление')),
                ('product', models.ForeignKey(verbose_name='Товар', to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('coming_products', models.ForeignKey(verbose_name='Партия', to='stock.ComingProducts')),
                ('order_products', models.ForeignKey(verbose_name='Заказ', to='orders.OrderProducts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка в интернете')),
                ('comment', models.TextField(verbose_name='Коммментарий')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coming',
            name='supplier',
            field=models.ForeignKey(to='stock.Supplier'),
            preserve_default=True,
        ),
    ]
