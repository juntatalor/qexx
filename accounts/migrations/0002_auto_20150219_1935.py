# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='middle_name',
            field=models.CharField(verbose_name='Отчество', max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=255),
            preserve_default=True,
        ),
    ]
