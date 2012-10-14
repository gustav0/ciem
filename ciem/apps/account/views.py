from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm,registerForm,ipaqForm, soyProfesionalForm, recordatorioForm
from ciem.apps.account.managers import antropometricosManager,frecuenciaConsumoManager,dataFrecuenciaConsumoManager,alimentoFrecuenciaManager
from ciem.apps.account.models import datosAntropometricos,frecuenciaConsumo,dataFrecuenciaConsumo,alimentoFrecuencia, datosRecordatorio
from ciem.apps.data.models import alimento
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import modelformset_factory
from django.core.mail import send_mail

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
def soyProfesional(request):
	if (request.method == 'POST'):
		form = soyProfesionalForm(request.POST, request.FILES)
		print form.errors
		if form.is_valid():
			form.save()
		return redirect(reverse('account_profile'))
	else:
		form = soyProfesionalForm
		nombre = request.user.get_full_name
		ctx = {'nombre':nombre,'form':form,'id':request.user.id}
		return render_to_response('account/soyProfesional.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def frecuencia(request):
	perfilFrecuencia = frecuenciaConsumo.objects.getById(request.user.id)
	alimento = ()
	preguntas = ()
	if perfilFrecuencia.exists():
		for p in perfilFrecuencia:
			progreso = p.progreso
		if progreso=='1':
			print "progreso 1"
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=26,max_num=26)
			alimento =	alimentoFrecuencia.objects.getById(1) 
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,2)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())

		elif progreso=='2':
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=17,max_num=17)
			alimento =	alimentoFrecuencia.objects.getById(2) 
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					print "validado"
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,3)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='3':
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=25,max_num=25)
			alimento =	alimentoFrecuencia.objects.getById(3) 
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,4)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='4':
			alimento =	alimentoFrecuencia.objects.getById(4) 
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=8,max_num=8)
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,5)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='5':
			alimento =	alimentoFrecuencia.objects.getById(5) 
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=27,max_num=27)
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,6)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='6':
			alimento =	alimentoFrecuencia.objects.getById(6) 
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=7,max_num=7)
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,7)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='7':
			alimento =	alimentoFrecuencia.objects.getById(7) 
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=20,max_num=20)
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,8)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
		elif progreso=='8':
			alimento =	alimentoFrecuencia.objects.getById(8) 
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=7,max_num=7)
			if request.method == 'POST':
				preguntas = preguntasFormSet(request.POST)
				if preguntas.is_valid():
					preguntas.save()
					perfilFrecuencia = frecuenciaConsumo.objects.upgradeProgreso(request.user.id,9)
					return HttpResponseRedirect("/frecuencia/")
			else:
				preguntas = preguntasFormSet(queryset=dataFrecuenciaConsumo.objects.none())
	else:
		if request.method == "POST":
			frecuenciaConsumo.objects.create(user=request.user,progreso='1')
			return HttpResponseRedirect("/frecuencia/")
		else:
			progreso = None
	ctx={'progreso':progreso,'alimento':alimento,'preguntas':preguntas,'perfilFrecuencia':perfilFrecuencia}
	return render_to_response('account/frecuenciaConsumo.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def recordatorio(request):
	alimentos = alimento.objects.all().order_by('nombre')
	ctx = {'alimentos':alimentos}
	return render_to_response('account/recordatorio24.html', ctx, context_instance=RequestContext(request))
