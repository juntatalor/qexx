# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20150328_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproducts',
            old_name='product',
            new_name='priced_product',
        ),
    ]
