# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20150328_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproducts',
            name='total',
        ),
    ]
