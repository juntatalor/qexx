# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное наименование')),
                ('code', models.CharField(max_length=3, verbose_name='Код')),
                ('code_a2', models.CharField(max_length=2, verbose_name='Код альфа-2')),
                ('code_a3', models.CharField(max_length=3, verbose_name='Код альфа-3')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
