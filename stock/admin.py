from django.contrib import admin
from django.db.models import Sum, Count
from autocomplete_light import ModelForm

from stock.models import Supplier, Coming, ComingProducts

# Register your models here.


class ComingProductsForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = ComingProducts


class ComingProductsInline(admin.TabularInline):
    model = ComingProducts
    form = ComingProductsForm


class ComingAdmin(admin.ModelAdmin):
    inlines = [ComingProductsInline]
    list_display = ('received', '__str__', 'supplier', 'date_ordered', 'date_shipped', 'date_received', 'price', 'amount', 'comment')
    list_display_links = ('__str__', )
    search_fields = ['supplier__name', 'coming_products__priced_product__name']

    def get_queryset(self, request):
        qs = super(ComingAdmin, self).get_queryset(request)
        return qs.annotate(price=Sum('coming_products__price'),
                           amount=Sum('coming_products__amount'),
                           amount_unique=Count('coming_products__amount'))

    def price(self, obj):
        return obj.price

    def amount(self, obj):
        return str(obj.amount) + ' (' + str(obj.amount_unique) + ')'

    price.short_description = 'Стоимость'
    amount.short_description = 'Количество'


class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ('__str__', 'link', 'comment')
    search_fields = ['name', 'link', 'comment']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Coming, ComingAdmin)
