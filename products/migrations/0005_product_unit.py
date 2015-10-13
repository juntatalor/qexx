# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(verbose_name='Единица измерения', default=1, to='products.Unit'),
            preserve_default=False,
        ),
    ]
