from django.conf.urls.defaults import *

from ciem.apps.homepage.feeds import archiveFeed
from django.contrib.auth.views import login, logout
from ciem.apps.account.forms import loginForm

urlpatterns = patterns('ciem.apps.homepage.views',
 url(r'^$', login , kwargs={'template_name':'homepage/index.html','authentication_form': loginForm}, name="homepage_index",),
 url(r'^nosotros/$', 'about', name="homepage_about"),
 url(r'^contacto/$', 'contact', name="homepage_contact"),
 url(r'^calculadora/$', 'calculadora', name="homepage_calculadora"),
 )

urlpatterns += patterns('',
	(r'^feed/archive/$', archiveFeed()),
)
