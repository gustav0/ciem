from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import  *
from django.conf import settings
from sitemaps import ciemSitemap, siteSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
	'ciem' : ciemSitemap,
	'pages' : siteSitemap(['homepage_contact', 'homepage_index'])
}
urlpatterns = patterns('',
  (r'^admin/', include(admin.site.urls)),
	(r'^', include('ciem.apps.homepage.urls')),
  (r'^', include('ciem.apps.account.urls')),
  (r'^', include('ciem.apps.nutricionista.urls')),
  (r'', include('ciem.apps.articles.urls')),
	(r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    # Examples:
    # url(r'^$', 'ciem.views.home', name='home'),
    # url(r'^ciem/', include('ciem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   	 
   	 (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT} ),
)
