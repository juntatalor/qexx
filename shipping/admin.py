from django.contrib import admin

from shipping.models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'code', 'code_a2', 'code_a3')
    search_fields = ['name', 'full_name', 'code', 'code_a2', 'code_a3']

admin.site.register(Country)