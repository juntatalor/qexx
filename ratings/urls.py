__author__ = 'Сергей'

from django.conf.urls import patterns, url

from ratings import views


urlpatterns = patterns('',
                       url(r'^add_rating/$', views.add_rating, name='add_rating'),
                       )
