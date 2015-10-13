# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20150606_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('additional_product', models.ForeignKey(to='products.PricedProduct', verbose_name='Товар для списания')),
                ('product', models.ForeignKey(to='products.Product', related_name='package', verbose_name='Товар')),
            ],
        ),
    ]
