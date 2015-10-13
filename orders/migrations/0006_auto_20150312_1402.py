# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20150312_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact_person',
            field=models.CharField(verbose_name='Контактное лицо', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(verbose_name='Email', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=50),
            preserve_default=True,
        ),
    ]
