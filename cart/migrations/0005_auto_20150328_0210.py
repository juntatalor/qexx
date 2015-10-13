# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20150326_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproducts',
            old_name='product',
            new_name='priced_product',
        ),
    ]
