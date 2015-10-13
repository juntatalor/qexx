# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150426_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(verbose_name='Адрес', blank=True),
        ),
    ]
