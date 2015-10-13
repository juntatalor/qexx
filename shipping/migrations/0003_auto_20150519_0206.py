# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_country_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
    ]
