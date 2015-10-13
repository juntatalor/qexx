# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='moderated',
            field=models.BooleanField(verbose_name='Модерация пройдена', default=False),
            preserve_default=False,
        ),
    ]
