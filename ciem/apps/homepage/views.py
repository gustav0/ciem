from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from django.template import RequestContext

def index(request):
	alimentos = alimento.objects.getByName("arroz blanco")
	ctx = { 'alimentos':alimentos }
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):
	return render_to_response('homepage/contact.html', context_instance=RequestContext(request))

def register(request):
	return render_to_response('homepage/register.html', context_instance=RequestContext(request))