__author__ = 'Сергей'

from django.conf.urls import patterns

from payment.gateways import gateways


urlpatterns = patterns('')

for name, gateway in list(gateways.items()):
    urlpatterns += gateway.urls