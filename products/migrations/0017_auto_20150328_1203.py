# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20150328_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedproduct',
            name='default',
            field=models.BooleanField(verbose_name='Свойство по умолчанию', default=False),
        ),
    ]
