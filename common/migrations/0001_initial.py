# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedSite',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=50)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('address', models.TextField(verbose_name='Адрес')),
                ('site', models.OneToOneField(verbose_name='Сайт', to='sites.Site')),
            ],
        ),
    ]
