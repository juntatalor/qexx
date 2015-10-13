from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ValidationError
from autocomplete_light import ModelForm

from products.models import Product, Category, ProductImage, PricedProduct, ProductVariation, ProductVariationValue, \
    PackageProduct

# Register your models here.


class ImageInline(admin.StackedInline):
    model = ProductImage


class PricedProductFormSet(BaseInlineFormSet):
    def clean(self):
        defaults = 0
        forms = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('default', False):
                    defaults += 1
                if form.cleaned_data:
                    forms += 1
        # Проверка количества цен для вариативного продукта
        # Приходится явно приводить типы, возможно есть более элегантное решение
        if self.data['type'] == str(Product.TYPE_COMMON) and forms > 1:
            raise ValidationError('Для обычного продукта должна быть установлена одна цена')
        # Проверка установки флагов "по умолчанию"
        if defaults > 1:
            raise ValidationError('Нельзя установить больше одной цены по умолчанию')


class PricedProductForm(ModelForm):
    class Meta:
        model = PricedProduct
        fields = ['default', 'variation_value', 'currency', 'price', 'status']

    def clean_variation_value(self):
        variation_value = self.cleaned_data['variation_value']
        if not self['DELETE'].data:
            if self.data['type'] == str(Product.TYPE_VARIATIVE) and not variation_value:
                raise ValidationError('Укажите свойство')
            elif self.data['type'] == str(Product.TYPE_COMMON) and variation_value:
                raise ValidationError('Для обычного продукта нельзя установить свойство')
        return variation_value


class PackageProductForm(ModelForm):
    class Meta:
        model = PackageProduct
        fields = '__all__'


class PricedProductInline(admin.TabularInline):
    form = PricedProductForm
    model = PricedProduct
    formset = PricedProductFormSet
    extra = 1


class PackageProductInline(admin.TabularInline):
    model = PackageProduct
    form = PackageProductForm


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, PricedProductInline, PackageProductInline]
    filter_horizontal = ('categories',)
    list_display = ('__str__', 'slug', 'sku', 'type', 'stock_amount')
    search_fields = ['name', 'slug']

    def get_queryset(self, request):
        return self.model.objects_detailed.get_queryset()

    def stock_amount(self, obj):
        return obj.stock_amount

    stock_amount.short_description = 'Остаток на складе'


class ProductVariationValueInline(admin.StackedInline):
    model = ProductVariationValue


class ProductVariationAdmin(admin.ModelAdmin):
    inlines = [ProductVariationValueInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductVariation, ProductVariationAdmin)
