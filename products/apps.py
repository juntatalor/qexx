__author__ = 'Сергей'

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from products.models import PricedProduct, ProductVariationValue
        import autocomplete_light
        autocomplete_light.register(PricedProduct,
                                    search_fields=['product__name'])
        autocomplete_light.register(ProductVariationValue,
                                    search_fields=['name', 'variation__name'])