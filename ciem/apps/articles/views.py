from django.shortcuts import get_object_or_404, render_to_response
from django import http
from django.template import RequestContext
from django.views.generic import list_detail
from ciem.apps.articles.models import *
from ciem.apps.articles.managers import ArticleManager
#from django.views.generic.date_based import object_list


def article_all(request):	
	ctx = {'lista':Article.objects.published()}
	return render_to_response('articles/article_all.html', ctx, context_instance=RequestContext(request))

def article_list(request, *args, **kwargs):
	from django.views.generic.list_detail import object_list
	category = get_object_or_404(Category, slug=kwargs.pop('category'))
	kwargs.update({
		'queryset': Article.objects.published(),
		# TODO: post_list paginate_by should be configurable.
		'paginate_by': 10,
		'allow_empty': True,
		'template_object_name': 'article',
	})
	return object_list(request, *args, **kwargs)

def article_detail(request, *args, **kwargs):
	from django.views.generic.date_based import object_detail
	category = get_object_or_404(Category, slug=kwargs.pop('category'))
	kwargs.update({
		'queryset': Article.objects.published(),
		'date_field': 'publish_date',
		'slug_field': 'slug',
		'template_object_name': 'article',
	})
	return object_list(request, *args, **kwargs)
	
	
def article_draft(request, article_id):
	if not request.user.is_authenticated():
		raise http.Http404()
	article = get_object_or_404(Article, pk=article_id, status=Article.DRAFT)
	return render_to_response([
		'articles/article_draft.html',
		'articles/article_detail.html',
	], {'article':article, 'is_draft': True}, context_instance=RequestContext(request))