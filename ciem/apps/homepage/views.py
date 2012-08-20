from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from django.template import RequestContext
from ciem.apps.homepage.forms import *

def index(request):
	alimentos = alimento.objects.getAll
	login_form = loginForm()
	ctx = {'login_form':login_form , 'alimentos':alimentos}
	return render_to_response('homepage/index.html', ctx,  context_instance=RequestContext(request))
"""{ 'alimentos':alimentos },"""
"""	alimentos = alimento.objects.getAll"""
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
	if request.method == "POST":
		register_form = registerForm(request.POST)
		if register_form.is_valid():
			success = True
			email = register_form.cleaned_data['email']
			password = register_form.cleaned_data['password']
	else:
		register_form = registerForm()
	ctx = {'register_form':register_form}
	return render_to_response('homepage/register.html', ctx, context_instance=RequestContext(request))