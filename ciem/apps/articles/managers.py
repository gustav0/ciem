from datetime import datetime
from django.db import models

class ArticleManager(models.Manager):

	def published(self):
		'Returns Articles that have a status of "published" and a publish date in the past.'
		from ciem.apps.articles.models import Article
		return self.get_query_set().filter(
			publish_date__lte=datetime.now(),
			status=Article.PUBLISHED).order_by('-publish_date')