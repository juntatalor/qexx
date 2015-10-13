# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20150328_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproducts',
            name='total',
        ),
    ]
