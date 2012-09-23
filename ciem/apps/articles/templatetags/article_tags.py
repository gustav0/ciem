from django import template

from ciem.apps.articles.models import *

register = template.Library()

class ArticlesNode(template.Node):
	
	def __init__(self, num, varname, filters=None, single_article=False):
		self.num = num
		self.varname = varname
		self.filters = filters
		self.single_article = single_article
		
	def render(self, context):
		articles = Article.objects.published()[:self.num]
		if self.filters:
			articles = articles.filter(**filters)
		if self.single_article:
			try:
				articles = articles[0]
			except IndexError:
				context[self.varname] = None
		context[self.varname] = articles
		return u''
		
@register.tag
def get_articles(parser, token):
	"""
	{% get_articles <num> as <varname> %}
	"""
	bits = token.split_contents()
	return ArticlesNode(bits[1], bits[3])
	
@register.tag
def get_latest_article(parser, token):
	"""
	{% get_latest_article as latest %}
	"""
	bits = token.split_contents()
	return ArticleNode(1, bits[2], single_article=True)