# coding: latin-1
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm,registerForm,ipaqForm, soyProfesionalForm, recordatorioForm, editRegisterForm
from ciem.apps.account.models import datosAntropometricos,frecuenciaConsumo,dataFrecuenciaConsumo,alimentoFrecuencia,userProfile,datosRecordatorio,ipaqResultado,ipaq as myipaq
from ciem.apps.data.models import alimento
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import modelformset_factory
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_protect

def register(request):
	form = registerForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		user.backend = settings.AUTHENTICATION_BACKENDS[0]
		login(request, user)
		return redirect(reverse('account_profile'))
	ctx={'form': form,}
	return render_to_response('account/register.html', ctx, context_instance=RequestContext(request))

def editRegister(request):
	if request.method == 'POST':
		form = registerForm(request.POST or None)
	else:
		usuario = userProfile.objects.get(id=request.user.id)
		dictionary = model_to_dict(usuario, fields=[], exclude=[])
		form = editRegisterForm(dictionary) 
	if form.is_valid():
		form.save()
	ctx={'form': form,}
	return render_to_response('account/editRegister.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def profile(request):
	antropometrico = datosAntropometricos.objects.getForPerfil(request.user.id)
	frecuencia = frecuenciaConsumo.objects.getById(request.user.id)
	ipaqr = myipaq.objects.getById(request.user.id)
	ctx={'profile':request.user.get_profile(),'antropometrico':antropometrico,'frecuencia':frecuencia}
	return render_to_response('account/profile.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def perfilAntropometrico(request):
	data = datosAntropometricos.objects.getByIdJoin(request.user.id)
	ctx = {'profile':request.user.get_profile(), 'data':data, }
	return render_to_response('account/perfilAntropometrico.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def antropometricos(request):
	form = antropometricosForm(request.POST or None)
	if form.is_valid():
		form.save(request)
		final = True
		apreciacion = None
	else:
		final = False
		apreciacion = None
	ctx= {'form':form, 'id':request.user.id,'final':final,'apreciacion':apreciacion }
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
			infouser = list(userProfile.objects.getUserJoin(request.user.id))
			user = str(infouser[0].first_name)+" "+str(infouser[0].last_name)
			url = "url"
			send_mail("Solicitd de Profesional","Nombre del solicintante:%s \nVisite el siguiente enlace para revisar mejor la información: %s" % (user,url), 'ciem.luz.mail@gmail.com',['ciem.luz.mail@gmail.com'])
			form.save()
			return redirect(reverse('account_profile'))
		else:
			ctx = {'form':form,'id':request.user.id}
			return render_to_response('account/soyProfesional.html', ctx, context_instance=RequestContext(request))
	else:
		form = soyProfesionalForm
		ctx = {'form':form,'id':request.user.id}
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
	form = recordatorioForm(request.POST or None)
	if request.method == 'POST':
		print request.POST
	alimentos = alimento.objects.all().order_by('nombre')
	ctx = {'form':form,'alimentos':alimentos}
	return render_to_response('account/recordatorio24.html', ctx, context_instance=RequestContext(request))
