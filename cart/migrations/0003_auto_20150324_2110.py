# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150324_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproducts',
            old_name='priced_product',
            new_name='product',
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Сумма', max_digits=10),
            preserve_default=False,
        ),
    ]
