# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150317_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductVariationValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length='255')),
                ('variation', models.ForeignKey(to='products.ProductVariation', verbose_name='Тип свойства')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='productpropertyvalue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productpropertyvalue',
            name='product_property',
        ),
        migrations.DeleteModel(
            name='ProductProperty',
        ),
        migrations.DeleteModel(
            name='ProductPropertyValue',
        ),
        migrations.AddField(
            model_name='productprice',
            name='variation_value',
            field=models.ForeignKey(to='products.ProductVariationValue', blank=True, verbose_name='Свойство', null=True),
            preserve_default=True,
        ),
    ]
