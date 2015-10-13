# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20150328_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productvariationvalue',
            options={'ordering': ['variation__name', 'name']},
        ),
    ]
