from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('ciem.apps.nutricionista.views',
 url(r'^perfiles/$', 'perfilUsuarios', name="nutricionista_perfilUsuarios"),
)
