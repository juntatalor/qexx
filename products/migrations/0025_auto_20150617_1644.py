# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.exceptions import ObjectDoesNotExist
import easy_thumbnails.fields


def move_images(apps, schema_editor):

    print('Moving main images')

    product_model = apps.get_model('products', 'Product')
    image_model = apps.get_model('products', 'ProductImage')
    for product in product_model.objects.all():
        try:
            img = image_model.objects.get(is_main=True, product=product)
        except ObjectDoesNotExist:
            print('Not found main image: ' + str(product))
            continue

        product.main_image = img.path
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20150614_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='images/product', blank=True),
        ),
        # Перенос изображений
        migrations.RunPython(move_images),
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
    ]
