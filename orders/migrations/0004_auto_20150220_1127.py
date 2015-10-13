# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150219_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='contact_person',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
