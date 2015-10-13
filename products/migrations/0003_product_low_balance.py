# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='low_balance',
            field=models.IntegerField(verbose_name='Низкий остатток', default=0),
            preserve_default=True,
        ),
    ]
