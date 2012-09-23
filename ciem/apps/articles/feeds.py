from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from django.db.models import permalink

from ciem.apps.articles.models import Article

class LatestArticlesFeed(Feed):
	"An RSS feed of the latest articles."
	# TODO: More fully implement the available hooks found at:
	# http://www.djangoproject.com/documentation/syndication_feeds/#feed-class-reference
	# categories, copyright, author_name, author_email, etc.
	
	def __init__(self, *args, **kwargs):
		self.site = Site.objects.get_current()
		super(LatestArticlesFeed, self).__init__(*args, **kwargs)
	
	def title(self):
		# TODO: Feed title should be configurable.
		return "%s: Latest articles" % self.site.name

	def description(self):
		# TODO: Feed description should be configurable.
		return "Latest articles from %s" % self.site.name

	@permalink
	def link(self):
		return ('feed', (), {'url': 'articles'})

	def items(self):
		# TODO: Number of feed items should be configurable.
		return Article.objects.published()[:10]
		
	def item_pubdate(self, item):
		return item.publish_date