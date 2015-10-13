# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import mptt.fields
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False)),
                ('image', models.ImageField(upload_to='images/category', verbose_name='Изображение')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', to='products.Category', null=True, blank=True, verbose_name='Родитель')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description_short', models.TextField(verbose_name='Описание')),
                ('description', models.TextField(verbose_name='Описание полное')),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False)),
                ('sku', models.CharField(max_length=255, verbose_name='Артикул')),
                ('stock_track', models.IntegerField(choices=[(-1, 'Не показывать остаток'), (0, 'Всегда доступно'), (1, 'Показывать точный остаток'), (2, 'Показывать остаток, когда товар заканчивается')], verbose_name='Метод отображения остатков', default=-1)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('path', models.ImageField(upload_to='images/product')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основное изображение')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(related_name='images', to='products.Product', verbose_name='Изображения')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Цена', max_digits=10)),
                ('currency', models.ForeignKey(to='payment.Currency',
                                               default=payment.models.Currency.get_main_currency_id,
                                               verbose_name='Валюта')),
                ('product', models.ForeignKey(related_name='prices', to='products.Product', verbose_name='Товар')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Имя свойства')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductPropertyValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.TextField(verbose_name='Значение')),
                ('product', models.ForeignKey(verbose_name='Товар', to='products.Product')),
                ('product_property', models.ForeignKey(verbose_name='Свойство', to='products.ProductProperty')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
