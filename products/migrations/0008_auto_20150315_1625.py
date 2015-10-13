# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150315_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='path',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='images/product'),
            preserve_default=True,
        ),
    ]
