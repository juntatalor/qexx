from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps import views

from accounts.forms import MyAuthenticationForm
from products.models import Product
from products.views import product_index

admin.site.login_form = MyAuthenticationForm
admin.site.login_template = 'accounts/login.html'


class ProductSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.date_updated

sitemaps = {
    'products': ProductSitemap
}

urlpatterns = patterns('',
                       url(r'^$', product_index),
                       url(r'^accounts/', include('accounts.urls', namespace='accounts')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^cart/', include('cart.urls', namespace='cart')),
                       url(r'^products/', include('products.urls', namespace='products')),
                       url(r'^orders/', include('orders.urls', namespace='orders')),
                       url(r'^search/', include('haystack.urls', namespace='search')),
                       url(r'^payment/', include('payment.urls', namespace='payment')),
                       url(r'^coupons/', include('coupons.urls', namespace='coupons')),
                       url(r'^ratings/', include('ratings.urls', namespace='ratings')),
                       url(r'^pages/', include('django.contrib.flatpages.urls')),
                       url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
                       url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps}),
                       url(r'^autocomplete/', include('autocomplete_light.urls')),
                       )

# Для дев-сервера попросим Джанго обслуживать наши медиа-файлы
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            )
