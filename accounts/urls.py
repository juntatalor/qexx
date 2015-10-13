from django.conf.urls import patterns, url
from accounts.forms import MyAuthenticationForm

from accounts import views

urlpatterns = patterns('',
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'accounts/login.html', 'authentication_form': MyAuthenticationForm},
                           name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': 'products:index'}, name='logout'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^signup/$', views.signup, name='signup'),
                       url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
                           name='password_reset'),
                       url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
                           name='password_reset_done'),
                       url(r'^password_reset/confirm/(?P<uidb64>[\w\-]+)/(?P<token>[\w]{1,13}-[\w]{1,20})/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           name='password_reset_confirm'),
                       url(r'password_reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),
                       url(r'^password_change/$', 'django.contrib.auth.views.password_change',
                           name='password_change'),
                       url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
                           name='password_change_done'),
)
