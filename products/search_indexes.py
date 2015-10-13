__author__ = 'Сергей'

from haystack import indexes
from products.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return Product.objects_detailed.get_queryset()
