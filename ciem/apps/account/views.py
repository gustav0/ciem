# coding: latin-1
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm,registerForm,ipaqForm, soyProfesionalForm, recordatorioForm, editRegisterForm, recuperarContrasenaForm, indicadoresDieteticosForm,frecuencia7Form
from ciem.apps.account.models import datosAntropometricos,frecuenciaConsumo,dataFrecuenciaConsumo,alimentoFrecuencia,userProfile,datosRecordatorio, indicadoresDieteticos,alimentoRecordatorio,ipaqResultado,ipaq as myipaq, preguntaSecreta, frecuencia7,indicadoresDieteticos
from ciem.apps.data.models import alimento
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import modelformset_factory
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_protect
from django.utils.encoding import smart_str, smart_unicode

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

def recuperarContrasena(request):
	bandera = 0
	pregunta = 'null'
	error = 0
	mensaje = ''
	form = recuperarContrasenaForm(request.POST or None)
	try:
		respuesta = request.POST['respuestaSecreta']
		cedula = request.POST['cedula']
		try:
			perfil = userProfile.objects.get(cedula=cedula, respuestaSecreta=respuesta)
			if perfil:
				user = User.objects.get(id=perfil.user_id)
				pass1 = request.POST['password1']
				pass2 = request.POST['password2']
				if pass1 and pass2 and pass1 == pass2:
					user.set_password(pass2)
					user.save()
					mensaje = 'Se cambio su contraseña correctamente, ahora lo invitamos a ingresar al sistema.'
				else:
					mensaje = 'No se pudo cambiar su contraseña, esto se debe a que los datos ingresados no son validos.'
			bandera = 2
		except:
			pregunta = request.POST['pregunta']
			error = 2		
	except:
		if request.method == 'GET':
			bandera = 1
		else:
			try:
				username = request.POST['username']
				usuario = User.objects.get(username=username)
				if (usuario):
					perfil = userProfile.objects.get(user_id=usuario.id)
					preg = preguntaSecreta.objects.get(id=perfil.preguntaSecreta)
					pregunta = preg.pregunta
			except User.DoesNotExist:
				bandera = 1
				error = 1

		#verificarDatos()
	ctx= {'form':form, 'bandera':bandera, 'pregunta':pregunta, 'error':error, 'mensaje':mensaje}
	return render_to_response('account/recuperarContrasena.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def profile(request):
	indicadores = indicadoresDieteticos.objects.getById(request.user.id)
	user = User.objects.get(pk=request.user.id)
	antropometrico = datosAntropometricos.objects.getForPerfil(request.user.id)
	recordatorios = datosRecordatorio.objects.getForPerfil(request.user.id)
	frecuencia = frecuenciaConsumo.objects.getById(request.user.id)
	ipaqr = ipaqResultado.objects.getResultados(request.user.id)
	recordatorios = datosRecordatorio.objects.getById(request.user.id)
	ctx={'profile':request.user.get_profile(),'antropometrico':antropometrico,'frecuencia':frecuencia,'ipaq':ipaqr, 'recordatorios':recordatorios,'indicadores':indicadores}
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
		apreciacion = datosAntropometricos.objects.getByIdJoin(request.user.id)
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
		form.save(request)
		form = ipaqResultado.objects.getResultados(request.user.id)
		final = True
	else:
		final = False
	ctx= {'form':form, 'id':request.user.id,'final':final }
	return render_to_response('account/ipaq.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def soyProfesional(request):
	if (request.method == 'POST'):
		form = soyProfesionalForm(request.POST, request.FILES)
		if form.is_valid():
			infouser = list(userProfile.objects.getUserJoin(request.user.id))
			user = smart_str(infouser[0].first_name)+" "+smart_str(infouser[0].last_name)
			url = "url"
		#	send_mail("Solicitd de Profesional","Nombre del solicintante:%s \nVisite el siguiente enlace para revisar mejor la información: %s" % (user,url), 'ciem.luz.mail@gmail.com',['ciem.luz.mail@gmail.com'])
			form.save()
			return redirect(reverse('account_profile'))
		else:
			ctx = {'form':form,'id':request.user.id}
			return render_to_response('account/soyProfesional.html', ctx, context_instance=RequestContext(request))
	else:
		form = soyProfesionalForm
		nombre = User.objects.get(id=request.user.id).first_name
		ctx = {'form':form,'id':request.user.id, 'nombre':nombre}
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
			preguntasFormSet = modelformset_factory(dataFrecuenciaConsumo,extra=26,max_num=26)
			alimento =	alimentoFrecuencia.objects.getById(1) 
			print alimento.count()
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
		elif progreso=='9':
			return HttpResponseRedirect('/felicidades/?mensaje=frecuencia')
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
		if form.is_valid():
			comidaDesayuno = request.POST.getlist('selCombo1')
			comidaMerienda1 = request.POST.getlist('selCombo2')
			comidaAlmuerzo = request.POST.getlist('selCombo3')
			comidaMerienda2 = request.POST.getlist('selCombo4')
			comidaCena = request.POST.getlist('selCombo5')
			comidaMerienda3 = request.POST.getlist('selCombo6')
			instance = form.save(request)
			for comida in comidaDesayuno:
				try:
					separado = comida.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance,alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print e
			for comida2 in comidaMerienda2:
				try:
					separado = comida2.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance, alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print e
			for comida3 in comidaAlmuerzo:
				try:
					separado = comida3.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance, alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print e
			for comida4 in comidaMerienda2:
				try:
					separado = comida4.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance, alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print e
			for comida5 in comidaCena:
				try:
					separado = comida5.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance, alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print e
			for comida6 in comidaMerienda3:
				try:
					separado = comida6.split('|')
					alimentoRecordar = alimentoRecordatorio(datosRecordatorio=instance, alimentoid=separado[0], namealimento=separado[1], tam=separado[2], cuandoComio=separado[3])
					alimentoRecordar.save()
				except Exception, e:
					print "ERROR"
			return HttpResponseRedirect('/felicidades/?mensaje=recordatorio')
	alimentos = alimento.objects.all().order_by('nombre')
	ctx = {'form':form,'alimentos':alimentos, 'id':request.user.id}
	return render_to_response('account/recordatorio24.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def indicadores(request):
	perfilIndicadores = indicadoresDieteticos.objects.getById(request.user.id)
	if not perfilIndicadores.exists():
		form = indicadoresDieteticosForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/felicidades/?mensaje=indicadores')
		ctx= {'form':form, 'id':request.user.id, }
		return render_to_response('account/indicadores.html', ctx, context_instance=RequestContext(request))
	return HttpResponseRedirect('/felicidades/')
	

def felicidades(request):
	getMensaje = request.GET.get('mensaje')
	mensaje = 'Opción no valida, le invitamos que ingrese a su perfil.'
	enlace = '/perfil/'
	if getMensaje == 'indicadores':
		mensaje = 'Usted ha finalizado exitosamente %s, le agradecemos su colaboración en nuestra investigación.' % ('los indicadores dieteticos')
		enlace = '/frecuencia/'
	if getMensaje == 'frecuencia7':
		mensaje = 'Usted ha finalizado exitosamente %s, le agradecemos su colaboración en nuestra investigación.' % ('la frecuencia de consumo 7 días')
		enlace = '/perfil/'
	if getMensaje == 'frecuencia':
		mensaje = 'Usted ha finalizado exitosamente %s, le agradecemos su colaboración en nuestra investigación.' % ('la frecuencia de consumo del mes')
		enlace = '/perfil/'
		#falta que este listo el frecuencia7 para poder redireccionar ahí.
	if getMensaje == 'recordatorio':
		mensaje = 'Usted ha finalizado exitosamente %s, le agradecemos su colaboración en nuestra investigación.' % ('el recordatorio de 24 horas')
		enlace = '/indicadores/'
	if getMensaje == 'publicar':
		mensaje = 'Usted a publicado exitosamente un articulo, puede regresar al perfil o ver los articulos publicados.'
		enlace = '/perfil/'
	ctx = {'mensaje':mensaje, 'enlace':enlace}
	return render_to_response('account/felicidades.html', ctx,  context_instance=RequestContext(request))

def frecuencia7(request):
	form = frecuencia7Form(request.POST or None)
	if form.is_valid():
			form.save()
			return HttpResponseRedirect('/felicidades/?mensaje=frecuencia7')
	ctx = {'form':form}
	return render_to_response('account/frecuencia7.html', ctx,  context_instance=RequestContext(request))

