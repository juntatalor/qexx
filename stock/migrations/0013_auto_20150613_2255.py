# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_auto_20150613_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockorderproducts',
            old_name='order_product',
            new_name='order_products',
        ),
    ]
