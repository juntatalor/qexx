# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailedsite',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
