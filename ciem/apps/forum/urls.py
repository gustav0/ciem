"""
URLConf for Django-Forum.

django-forum assumes that the forum application is living under
/forum/.

Usage in your base urls.py:
    (r'^forum/', include('forum.urls')),

"""

from django.conf.urls.defaults import *
from ciem.apps.forum.models import Forum


urlpatterns = patterns('',
    url(r'^forum/$', 'ciem.apps.forum.views.forums_list', name='forum_index'),
    url(r'^prueba/$','ciem.apps.forum.views.prueba', name='forum_prueba'),
    url(r'^thread/(?P<thread>[0-9]+)/$', 'ciem.apps.forum.views.thread', name='forum_view_thread'),
    url(r'^thread/(?P<thread>[0-9]+)/reply/$', 'ciem.apps.forum.views.reply', name='forum_reply_thread'),

    url(r'^subscriptions/$', 'ciem.apps.forum.views.updatesubs', name='forum_subscriptions'),

    url(r'^(?P<slug>[-\w]+)/$', 'ciem.apps.forum.views.forum', name='forum_thread_list'),
    url(r'^(?P<forum>[-\w]+)/new/$', 'ciem.apps.forum.views.newthread', name='forum_new_thread'),

    url(r'^([-\w/]+/)(?P<forum>[-\w]+)/new/$', 'ciem.apps.forum.views.newthread'),
    url(r'^([-\w/]+/)(?P<slug>[-\w]+)/$', 'ciem.apps.forum.views.forum', name='forum_subforum_thread_list'),

    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemap_dict}),
    #(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemap_dict}),
)
