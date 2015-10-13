# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20150326_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comingproducts',
            old_name='product',
            new_name='priced_product',
        ),
        migrations.RenameField(
            model_name='stockrecord',
            old_name='product',
            new_name='priced_product',
        ),
    ]
