# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20150617_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(verbose_name='Популярный товар', default=False),
            preserve_default=False,
        ),
    ]
