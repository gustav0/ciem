from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from django.template import RequestContext
from ciem.apps.homepage.forms import *
from django.core.mail import send_mail

def index(request):
	alimentos = alimento.objects.getAll
	#login_form = loginForm()
	ctx = {'alimentos':alimentos}
	return render_to_response('homepage/index.html', ctx,  context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):
	success = False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		contact_form = contactForm(request.POST)
		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			title = contact_form.cleaned_data['title']
			text = contact_form.cleaned_data['text']

			send_mail(title,"Text message: %s" % (text), email,['ciem.luz.mail@gmail.com'])
	else:
		contact_form = contactForm()
	ctx = {'contact_form':contact_form, 'email':email, 'title':title, 'text':text, 'success':success}
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


#CSRF EN CONTACTO * TUTORIAL
def csrf_malo(request, reason=''):
	ctx= {'reason':reason}
	return render_to_response('csrf/rejected.html',ctx)

