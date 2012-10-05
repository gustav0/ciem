from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm,registerForm,ipaqForm,frecuenciaForm
from ciem.apps.account.managers import antropometricosManager,frecuenciaConsumoManager,dataFrecuenciaConsumoManager,alimentoFrecuenciaManager
from ciem.apps.account.models import datosAntropometricos,frecuenciaConsumo,dataFrecuenciaConsumo,alimentoFrecuencia
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import modelformset_factory


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
	ctx={'profile':request.user.get_profile(),'usuario':request.user.get_full_name,}
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
		form.save(request)
	ctx= {'form':form, 'id':request.user.id, }
	return render_to_response('account/datosAntropometricosForm.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def nutricionistas(request):
	ctx= {}	
	return render_to_response('account/nutricionistas.html', ctx, context_instance=RequestContext(request))
	
@login_required(login_url='/login')
def ipaq(request):
	form = ipaqForm(request.POST or None)
	if form.is_valid():
		form.save()
	ctx= {'form':form, 'id':request.user.id, }
	return render_to_response('account/ipaq.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def frecuencia(request):
	perfilFrecuencia = frecuenciaConsumo.objects.getById(request.user.id)
	alimento = ()
	preguntas = ()
	preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo)
	if perfilFrecuencia.exists():
		for p in perfilFrecuencia:
			progreso = p.progreso
		if progreso=='1':
			print "progreso 1"
			preguntas = preguntasFormSet(request.POST or None)
			print preguntasFormSet
			if preguntas.is_valid():
				print "entre"
				preguntas.save()
			else:
				print "no entre"
				alimento =	alimentoFrecuencia.objects.getById(1) 
		elif progreso=='2':
			print "seccion 2"
	else:
		if request.method == "POST":
			frecuenciaConsumo.objects.create(user=request.user,progreso='1')
			progreso = '1'
		else:
			progreso = None
	ctx={'progreso':progreso,'alimento':alimento,'preguntas':preguntas,'perfilFrecuencia':perfilFrecuencia}
	return render_to_response('account/frecuenciaConsumo.html', ctx, context_instance=RequestContext(request))
