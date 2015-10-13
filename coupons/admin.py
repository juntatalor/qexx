from django.contrib import admin
from django.db.models import Count

from coupons.models import Coupon

# Register your models here.


class CouponAdmin(admin.ModelAdmin):
    list_display = ('active', '__str__', 'date', 'expire_date', 'max_usage', 'used')
    list_display_links = ('__str__',)
    search_fields = ['code', 'comment']

    def get_queryset(self, request):
        qs = super(CouponAdmin, self).get_queryset(request)
        return qs.annotate(used=Count('orders'))

    def used(self, obj):
        return obj.used

    used.short_description = 'Количество использований'

admin.site.register(Coupon, CouponAdmin)
