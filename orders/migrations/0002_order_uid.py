# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.CharField(max_length=20, verbose_name='Идентификатор', default=''),
            preserve_default=False,
        ),
    ]
