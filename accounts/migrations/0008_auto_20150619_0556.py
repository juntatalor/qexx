# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shipping.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(verbose_name='Страна', to='shipping.Country', default=shipping.models.Country.default_country_id, blank=True),
        ),
    ]
