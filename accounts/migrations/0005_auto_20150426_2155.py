# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150328_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, blank=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='middle_name',
            field=models.CharField(max_length=255, blank=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=255, blank=True, verbose_name='Телефон'),
        ),
    ]
