# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('image', models.ImageField(upload_to='images/rating', verbose_name='Изображение')),
                ('product', models.ForeignKey(related_name='ratings', to='products.Product', verbose_name='Товар')),
                ('user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
