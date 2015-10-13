__author__ = 'Сергей'

from django.conf.urls import patterns, url

from coupons import views


urlpatterns = patterns('',
                       url(r'add_to_cart/$', views.add_coupon, name='add_coupon'),
                       url(r'remove_from_cart/$', views.remove_coupon, name='remove_coupon'),
                       )

