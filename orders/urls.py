from django.conf.urls import patterns, url

from orders import views


urlpatterns = patterns('',
                       url(r'^$', views.order_index, name='index'),
                       url(r'^(?P<uid>\w+)/$', views.direct_view, name='direct_view'),
                       url(r'^print/cheque/$', views.print_cheque, name='print_cheque'),
                       )
