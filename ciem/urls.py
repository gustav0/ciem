from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import  *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^', include('ciem.apps.homepage.urls')),
    # Examples:
    # url(r'^$', 'ciem.views.home', name='home'),
    # url(r'^ciem/', include('ciem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   	 (r'^admin/', include(admin.site.urls)),
   	 (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT} ),
)
