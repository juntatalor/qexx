# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основная страна'),
            preserve_default=True,
        ),
    ]
