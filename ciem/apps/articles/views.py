from django.shortcuts import get_object_or_404, render_to_response
from django import http
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ciem.apps.articles.models import *
from ciem.apps.articles.forms import * 


def nuevoArticulo(request):
	form = articleNuevoForm(request.POST or None)
	print request.POST
	if form.is_valid():
		articulo = form.save(commit=False)
		articulo.author = request.user
		articulo.save()
		return HttpResponseRedirect('/felicidades/?mensaje=publicar')
	ctx= {'form':form,'id':request.user.id}
	return render_to_response('articles/publicar.html', ctx, context_instance=RequestContext(request))

def article_all(request):	
	articulosPublicados = Article.objects.published()
	ctx = {'lista':articulosPublicados}
	return render_to_response('articles/article_all.html', ctx, context_instance=RequestContext(request))

def article_list(request, *args, **kwargs):
	from django.views.generic.list_detail import object_list
	nuevo_object_list = object_list
	category = get_object_or_404(Category, slug=kwargs.pop('category'))
	kwargs.update({
		'queryset': Article.objects.published(),
		# TODO: post_list paginate_by should be configurable.
		'paginate_by': 10,
		'allow_empty': True,
		'template_object_name': 'article',
	})
	return nuevo_object_list(request, *args, **kwargs)

def article_detail(request, *args, **kwargs):
	from django.views.generic.date_based import object_detail
	nuevo_object_detail = object_detail
	category = get_object_or_404(Category, slug=kwargs.pop('category'))
	kwargs.update({
		'queryset': Article.objects.published(),
		'date_field': 'publish_date',
		'slug_field': 'slug',
		'template_object_name': 'article',
	})
	return nuevo_object_detail(request, *args, **kwargs)
	
	
def article_draft(request, article_id):
	if not request.user.is_authenticated():
		raise http.Http404()
	article = get_object_or_404(Article, pk=article_id, status=Article.DRAFT)
	return render_to_response([
		'articles/article_draft.html',
		'articles/article_detail.html',
	], {'article':article, 'is_draft': True}, context_instance=RequestContext(request))