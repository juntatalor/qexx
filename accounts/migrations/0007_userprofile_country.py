# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shipping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_country_is_main'),
        ('accounts', '0006_auto_20150426_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(verbose_name='Страна', default=shipping.models.Country.default_country_id, to='shipping.Country'),
        ),
    ]
