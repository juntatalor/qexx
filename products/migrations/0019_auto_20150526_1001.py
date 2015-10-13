# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20150426_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
