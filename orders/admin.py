from django.contrib import admin
from django import forms
from django.db.models import Sum, Count
from autocomplete_light import ModelForm

from orders.models import Order, OrderProducts
from orders.signals import order_post_save
from payment.gateways import gateways
from shipping.methods import methods


class OrderProductsForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = OrderProducts


class OrderProductInline(admin.TabularInline):
    model = OrderProducts
    form = OrderProductsForm


class OrderForm(forms.ModelForm):
    payment_method = forms.ChoiceField(label='Метод оплаты',
                                       choices=[(name, gw.name) for name, gw in gateways.items()])
    shipping_method = forms.ChoiceField(label='Метод доставки',
                                        choices=[(name, mt.name) for name, mt in methods.items()])

    class Meta:
        fields = '__all__'
        model = Order


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    inlines = [OrderProductInline]
    list_display = (
        '__str__', 'contact', 'order_status', '_shipping_method', '_payment_method', 'payment_status', 'price',
        'discount', 'amount')
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'email', 'shipping_address',
                     'order_products__priced_product__name']

    def save_formset(self, request, form, formset, change):
        super(OrderAdmin, self).save_formset(request, form, formset, change)
        if formset.model == OrderProducts:
            order_post_save.send(sender=self.model.__class__, instance=form.instance)

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        return qs.annotate(price=Sum('order_products__price'),
                           amount=Sum('order_products__amount'),
                           unique_amount=Count('order_products__id'))

    def _shipping_method(self, obj):
        try:
            return methods[obj.shipping_method].name
        except KeyError:
            return '-'

    def _payment_method(self, obj):
        try:
            return gateways[obj.payment_method].name
        except KeyError:
            return '-'

    def price(self, obj):
        return obj.price

    def amount(self, obj):
        return str(obj.amount) + ' (' + str(obj.unique_amount) + ')'

    def contact(self, obj):
        return obj.user or obj.email

    price.short_description = 'Стоимость'
    amount.short_description = 'Количество товаров'
    contact.short_description = 'Получен от'
    _shipping_method.short_description = 'Метод доставки'
    _payment_method.short_description = 'Метод оплаты'


admin.site.register(Order, OrderAdmin)
