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
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('status', models.IntegerField(choices=[(0, 'Заказ получен'), (1, 'Заказ оплачен'), (2, 'Обработка'), (3, 'Заказ отправлен'), (4, 'Заказ получен'), (5, 'Заказ отменен')], verbose_name='Статус заказа')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone', models.CharField(max_length=50)),
                ('user_comment', models.TextField(verbose_name='Комментарий покупателя')),
                ('staff_comment', models.TextField(verbose_name='Комментарий персонала')),
                ('currency', models.ForeignKey(to='payment.Currency',
                                               default=payment.models.Currency.get_main_currency_id,
                                               verbose_name='Валюта')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Пользователь')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Цена', max_digits=10)),
                ('order', models.ForeignKey(related_name='order_products', to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(verbose_name='Товар', to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
