from django.conf.urls import patterns, url

from cart import views


urlpatterns = patterns('',
                       url(r'^$', views.view_cart, name='view'),
                       url(r'^add/$', views.add_to_cart, name='add'),
                       url(r'^remove/$', views.remove_from_cart, name='remove'),
                       url(r'^update/$', views.update_cart, name='update'),
                       url(r'^checkout/$', views.checkout, name='checkout'),
                       url(r'^update_checkout/$', views.update_checkout, name='update_checkout'),
                       # Для ajax обновления виджета корзины
                       url(r'^summary/$', views.get_cart_summary, name='get_cart_summary'),
                       )
