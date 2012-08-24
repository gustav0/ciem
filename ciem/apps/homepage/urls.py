from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

from ciem.apps.homepage.feeds import archiveFeed

urlpatterns = patterns('ciem.apps.homepage.views',
 url(r'^$', 'index', name="homepage_index"),
 url(r'^about/$', 'about', name="homepage_about"),
 url(r'^contact/$', 'contact', name="homepage_contact"),
 url(r'^profile/$', 'profile', name="homepage_profile"),
 url(r'^register/$', 'register', name="homepage_register"),
 url(r'^calculadora/$', 'calculadora', name="homepage_calculadora"),
)

urlpatterns += patterns('',
	url(r'login$', login, kwargs={'template_name':'homepage/login.html'}, name="homepage_login"),
	url(r'logout$', logout, kwargs={'next_page':'login'}, name="homepage_logout"),
	(r'^feed/archive/$', archiveFeed()),
)