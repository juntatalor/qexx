# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def remove_images(apps, schema_editor):
    product_model = apps.get_model('products', 'Product')
    for product in product_model.objects.all(). \
            prefetch_related('images'):
        for image in product.images.all():
            if image.path == product._main_image:
                image.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0028_auto_20150620_1035'),
    ]

    operations = [
        migrations.RunPython(remove_images),
    ]
