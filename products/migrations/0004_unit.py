# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_low_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
