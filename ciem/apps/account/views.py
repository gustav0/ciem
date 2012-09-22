from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm, registerForm, ipaqForm
from ciem.apps.account.managers import antropometricosManager
from ciem.apps.account.models import datosAntropometricos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register(request):
	form = registerForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		user.backend = settings.AUTHENTICATION_BACKENDS[0]
		login(request, user)
		return redirect(reverse('account_profile'))
	ctx={'form': form,}
	return render_to_response('account/register.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def profile(request):
	ctx={'profile':request.user.get_profile(),'usuario':request.user,}
	return render_to_response('account/profile.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def perfilAntropometrico(request):
	data = datosAntropometricos.objects.getById(request.user.id)
	paginator = Paginator(data, 2)
	numero_pagina = request.GET.get('page',1)
	try:
		pagina = paginator.page(numero_pagina)
	except EmptyPage:
		pagina = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		pagina = paginator.page(1)
	ctx = {'profile':request.user.get_profile(), 'pagina':pagina, }
	return render_to_response('account/perfilAntropometrico.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def antropometricos(request):
	form = antropometricosForm(request.POST or None)
	if form.is_valid():
		form.save()
	ctx= {'form':form, 'id':request.user.id, }
	return render_to_response('account/datosAntropometricosForm.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def nutricionistas(request):
	ctx= {}	
	return render_to_response('account/nutricionistas.html', ctx, context_instance=RequestContext(request))
	
def ipaq(request):
	form = ipaqForm(request.POST or None)
	if form.is_valid():
		form.id
		form.save()
	ctx= {'form':form, 'id':request.user.id, }
	return render_to_response('account/ipaq.html', ctx, context_instance=RequestContext(request))

	