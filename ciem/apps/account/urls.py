from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('ciem.apps.account.views',
 url(r'^profile/$', 'profile', name="account_profile"),
 url(r'^register/$', 'register', name="account_register"),
 url(r'^antropometricos/$', 'antropometricos', name="account_datosAntropometricos"),
 url(r'^diagnostico/$', 'perfilAntropometrico', name="account_perfilAntropometrico"),
)

urlpatterns += patterns('',
  url(r'login$', login, kwargs={'template_name':'account/login.html'}, name="account_login"),
  url(r'logout$', logout, kwargs={'next_page':'login'}, name="account_logout"),
 )