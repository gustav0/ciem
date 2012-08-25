from django.conf.urls.defaults import *

from ciem.apps.homepage.feeds import archiveFeed

urlpatterns = patterns('ciem.apps.homepage.views',
 url(r'^$', 'index', name="homepage_index"),
 url(r'^about/$', 'about', name="homepage_about"),
 url(r'^contact/$', 'contact', name="homepage_contact"),
 url(r'^register/$', 'register', name="homepage_register"),
 url(r'^calculadora/$', 'calculadora', name="homepage_calculadora"),
)

urlpatterns += patterns('',
	(r'^feed/archive/$', archiveFeed()),
)