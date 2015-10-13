# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Заказ получен'), (2, 'Обработка'), (3, 'Заказ отправлен'), (4, 'Заказ получен'), (5, 'Заказ отменен')], default=0, verbose_name='Статус заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=0, verbose_name='Метод оплаты', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(choices=[(0, 'Не оплачен'), (1, 'Обработка платежа'), (2, 'Оплачен')], default=0, verbose_name='Статус оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.CharField(default=0, verbose_name='Метод доставки', max_length=255),
            preserve_default=False,
        ),
    ]
