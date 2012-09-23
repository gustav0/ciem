from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ciem.apps.tagging.fields import TagField

from ciem.apps.articles.managers import ArticleManager

class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(blank=True, max_length=500)
	slug = models.SlugField(max_length=100, unique=True)
	
	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return ('article_list', (), {'category':self.slug})
		
	class Meta:
		verbose_name_plural = 'categories'
		ordering = ('name',)

		
class Article(models.Model):
	
	DRAFT = 'draft'
	PUBLISHED = 'published'
	
	objects = ArticleManager()	
	# TODO: Add tagging once it's updated to 1.0
	# TODO: Add ``Location`` model
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=200)
	body = models.TextField()
	tags = TagField(max_length=100, blank=True)
	publish_date = models.DateTimeField(default=datetime.now, help_text=u'You may future-date articles to enable scheduled publishing.')
	status = models.CharField(max_length=100, choices=((DRAFT, 'Draft'),(PUBLISHED, 'Published')), default=DRAFT, help_text=u'Only articles with "Published" status will be shown on site.')
	author = models.ForeignKey(User)
	featured = models.BooleanField(default=False)
	related_articles = models.ManyToManyField('Article', blank=True, null=True)
	slug = models.SlugField(max_length=200, help_text=u'It it recommended to use the default slug.')
	#allow_comments = models.BooleanField(default=True)
	summary = models.CharField(blank=True, max_length=500)
	snippet = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.title
		
	def save(self):
		super(Article, self).save()
		if self.is_published():
			from ciem.apps.articles.pings import send_pings
			send_pings(self)
		
	def is_published(self):
		return self.status == Article.PUBLISHED and self.publish_date <= datetime.now()
		
	@models.permalink
	def get_absolute_url(self):
		if self.is_published():
			return ('article_detail', (), {
				'category': self.category.slug,
				'year': self.publish_date.strftime('%Y'),
				'month': self.publish_date.strftime('%b').lower(),
				'day': self.publish_date.strftime('%d'),
				'slug': self.slug
			})
		else:
			return ('article_draft', (), {
				'article_id': self.id
			})
	
	#def approved_comments(self):
	#	try:
	#		from comments.models import Comment
	#		return Comment.objects.approved_for_object(self)
	#	except ImportError:
	#		return []
	
	class Meta:
		ordering = ('publish_date',)