# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shipping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_country_is_main'),
        ('orders', '0013_order_shipping_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.ForeignKey(verbose_name='Страна', default=shipping.models.Country.default_country_id, to='shipping.Country'),
        ),
    ]
