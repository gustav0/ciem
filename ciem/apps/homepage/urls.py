from django.conf.urls.defaults import *

from ciem.apps.homepage.feeds import archiveFeed

urlpatterns = patterns('ciem.apps.homepage.views',
 url(r'^$', 'index', name="homepage_index"),
 url(r'^nosotros/$', 'about', name="homepage_about"),
 url(r'^contacto/$', 'contact', name="homepage_contact"),
 url(r'^calculadora/$', 'calculadora', name="homepage_calculadora"),
  )

urlpatterns += patterns('',
	(r'^feed/archive/$', archiveFeed()),
)
