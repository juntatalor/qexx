# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20150617_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='main_image',
            new_name='_main_image',
        ),
    ]
