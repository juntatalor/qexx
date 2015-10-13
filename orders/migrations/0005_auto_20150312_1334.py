# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150220_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Заказ получен'), (1, 'Обработка'), (2, 'Заказ отправлен'), (3, 'Заказ получен'), (4, 'Заказ отменен')], verbose_name='Статус заказа'),
            preserve_default=True,
        ),
    ]
