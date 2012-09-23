from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from ciem.apps.data.models import alimento

from datetime import datetime

class ciemSitemap(Sitemap):
	chagefreq = 'never'
	priority = 0.5
	def items(self):
		return alimento.objects.all()
	def location(self, obj):
		return '/'

class siteSitemap(Sitemap):
	def __init__(self, names):
		self.names = names

	def items(self):
		return self.names

	def lastmod(self, obj):
		return datetime.now()
		
	def location(self, obj):
		return reverse(obj)


