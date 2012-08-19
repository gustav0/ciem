from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from django.template import RequestContext
from ciem.apps.homepage.forms import contactForm

def index(request):
	alimentos = alimento.objects.getAll
	ctx = { 'alimentos':alimentos }
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):
	if request.method == "POST":
		contact_form = contactForm(request.POST)
		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			title = contact_form.cleaned_data['title']
			text = contact_form.cleaned_data['text']
	else:
		contact_form = contactForm()
	ctx = {'contact_form':contact_form}
	return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

def register(request):
	return render_to_response('homepage/register.html', context_instance=RequestContext(request))