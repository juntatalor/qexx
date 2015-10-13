# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import payment.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('uid', models.CharField(max_length=32, verbose_name='Идентификатор')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('currency', models.ForeignKey(to='payment.Currency',
                                               default=payment.models.Currency.get_main_currency_id,
                                               verbose_name='Валюта')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Пользователь')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('cart', models.ForeignKey(related_name='cart_products', to='cart.Cart')),
                ('product', models.ForeignKey(related_name='cart_products', to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
