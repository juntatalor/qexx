# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(max_digits=10, verbose_name='Скидка', decimal_places=2, default=0),
            preserve_default=False,
        ),
    ]
