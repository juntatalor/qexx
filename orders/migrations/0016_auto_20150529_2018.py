# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_cost',
            new_name='shipping_price',
        ),
    ]
