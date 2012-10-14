from django.conf.urls.defaults import *

urlpatterns = patterns('ciem.apps.data.views',
 url(r'^peso/$', 'pesoAlimento', name="data_pesoAlimento"),
)