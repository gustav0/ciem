from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from django.template import RequestContext
from ciem.apps.homepage.forms import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def index(request):
	ctx = {}
	return render_to_response('homepage/index.html', ctx,  context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/about.html', context_instance=RequestContext(request))
	
def contact(request):
	success = False
	email = ""
	asunto = ""
	texto = ""
	if request.method == "POST":
		contact_form = contactForm(request.POST)
		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			asunto = contact_form.cleaned_data['asunto']
			texto = contact_form.cleaned_data['texto']
			send_mail(asunto,"Email contacto: %s \nAsunto: %s \nTexto: %s" % (email,asunto,texto), 'ciem.luz.mail@gmail.com',['ciem.luz.mail@gmail.com'])
	else:
		contact_form = contactForm()
	ctx = {'contact_form':contact_form, 'email':email, 'asunto':asunto, 'texto':texto, 'success':success}
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

@login_required
def profile(request):
	ctx={}
	return render_to_response('homepage/profile.html', ctx, context_instance=RequestContext(request))

