# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_pricedproduct_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariationvalue',
            name='name',
            field=models.CharField(verbose_name='Наименование', max_length=255),
            preserve_default=True,
        ),
    ]
