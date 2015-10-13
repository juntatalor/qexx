# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20150328_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coming',
            name='supplier',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Поставщик', to='stock.Supplier'),
        ),
    ]
