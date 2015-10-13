# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150324_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricedproduct',
            name='status',
            field=models.IntegerField(choices=[(0, 'Черновик'), (1, 'Опубликован')], default=0, verbose_name='Статус'),
            preserve_default=True,
        ),
    ]
