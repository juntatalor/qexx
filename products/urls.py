from django.conf.urls import patterns, url

from products import views


urlpatterns = patterns('',
                       url(r'^$', views.product_index, name='index'),
                       url(r'^popular/$', views.product_popular, name='popular'),
                       url(r'^new/$', views.product_new, name='new'),
                       url(r'^(?P<slug>[\w-]+)/$', views.product_detail, name='detail'),
                       url(r'^category/(?P<slug>[\w-]+)/$', views.category_detail, name='category'),
                       )
