# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('short_name', models.CharField(max_length=255, verbose_name='Сокращение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основная валюта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('rate', models.DecimalField(decimal_places=3, verbose_name='Курс', max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('currency', models.ForeignKey(related_name='exchange_rate', to='payment.Currency', verbose_name='Валюта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
