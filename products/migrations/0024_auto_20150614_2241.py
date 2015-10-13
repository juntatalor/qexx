# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_packageproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageproduct',
            old_name='amount',
            new_name='distribute_amount',
        ),
    ]
