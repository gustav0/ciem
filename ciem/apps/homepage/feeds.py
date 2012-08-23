from django.contrib.syndication.views import Feed

from ciem.apps.data.models import alimento

class archiveFeed(Feed):
	nombre = 'Archive Feed'
	description = 'Archive Feed'
	link = '/archive/'

	def items(self):
		return alimento.objects.all()

	def item_link(self, item):
		return '/archive/'

	def item_nombre(self, item):
		return item.nombre

	def item_description(self, item):
		return 'hola'