from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('ciem.apps.account.views',
 url(r'^profile/$', 'profile', name="account_profile"),
 url(r'^register/$', 'register', name="account_register"),
 url(r'^antropometricos/$', 'antropometricos', name="account_datosAntropometricos"),
 url(r'^diagnostico/$', 'perfilAntropometrico', name="account_perfilAntropometrico"),
 url(r'^nutricionistas/$', 'nutricionistas', name="account_nutricionistas"),
 url(r'^ipaq/$', 'ipaq', name="account_ipaq"),
 url(r'^frecuencia/$', 'frecuencia', name="account_frecuencia"),
 url(r'^recordatorio/$', 'recordatorio', name='account_recordatorio'),
 url(r'^profesional/$', 'soyProfesional', name="account_soyProfesional"),
 url(r'^edit/$', 'editRegister', name="account_editRegister"),
)

urlpatterns += patterns('',
  url(r'login$', login, kwargs={'template_name':'account/login.html'}, name="account_login"),
  url(r'logout$', logout, kwargs={'next_page':'login'}, name="account_logout"),
 )