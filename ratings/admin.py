from django.contrib import admin

from ratings.models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('moderated', '__str__', 'product', 'user', 'rating', 'date')
    list_display_links = ('__str__', )

admin.site.register(Rating, RatingAdmin)
