# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150322_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='productprice',
            name='default',
            field=models.BooleanField(verbose_name='Свойство по уомлчанию', default=False),
            preserve_default=True,
        ),
    ]
