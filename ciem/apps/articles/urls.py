from django.conf.urls.defaults import *
from ciem.apps.articles import views

urlpatterns = patterns('',
	url(r'^publicar/$',views.nuevoArticulo, name="nuevoArticulo"),
	url(r'^articleall/$', views.article_all, name='article_all'),
	url(r'^(?P<category>[-\w]+)/$',views.article_list, name="article_list"),
	url(r'^(?P<category>[-\w]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',views.article_detail, name="article_detail"),
	url(r'^drafts/(?P<article_id>\d+)/$',views.article_draft, name="article_draft"),
)