from django.conf.urls.defaults import *

urlpatterns = patterns('ciem.apps.homepage.views',
 url(r'^$', 'index', name="homepage_index"),
 url(r'^about/$', 'about', name="homepage_about"),
 url(r'^register/$', 'register', name="homepage_register"),
  url(r'^contact/$', 'contact', name="homepage_contact")
)
