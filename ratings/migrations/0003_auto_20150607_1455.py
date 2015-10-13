# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rating_moderated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(verbose_name='Рейтинг', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
