# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usernameaddition'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, verbose_name='email address', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', related_name='user_set', related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, verbose_name='last login', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(unique=True, verbose_name='username', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        ),
    ]
