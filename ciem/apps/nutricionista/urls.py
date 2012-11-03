from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('ciem.apps.nutricionista.views',
 url(r'^perfiles/$', 'perfilUsuarios', name="nutricionista_perfilUsuarios"),
 url(r'^peticiones/$', 'verPeticiones', name="nutricionista_peticiones"),
 url(r'^busqueda/$', 'busqueda', name="nutricionista_busqueda"),
)
