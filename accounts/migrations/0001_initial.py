# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import accounts.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], unique=True, max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_token', models.CharField(max_length=40, default=accounts.models.new_email_token, unique=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
    ]
