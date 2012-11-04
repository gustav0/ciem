from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger
from ciem.apps.account.models import datosAntropometricos,antropometricosResultado,userProfile,ipaqResultado,ipaq,frecuenciaConsumo, profesional, indicadoresDieteticos
from django.contrib.auth.models import User, Group
from ciem.apps.nutricionista.forms import *

@login_required(login_url='/login')
def verPeticiones(request):
	getUser = request.GET.get('user',1)
	aceptar = request.GET.get('a',0)
	if (int(aceptar) == 1):
		profesional.objects.filter(user_id = getUser).update(status='aceptado')
		persona = User.objects.get(id = getUser)
		g = Group.objects.get(name='profesional') 
		g.user_set.add(persona)
	elif (int(aceptar) == 2):
		profesional.objects.filter(user_id = getUser).update(status='rechazado')
	peticiones = profesional.objects.filter(status = 'pendiente')
	usuario = User.objects.all()
	perfil = userProfile.objects.all()
	ctx= {'peticiones':peticiones,'usuario':usuario, 'perfil':perfil}	
	return render_to_response('nutricionista/peticiones.html', ctx, context_instance=RequestContext(request))

def busqueda(request):
	form = busquedaForm(request.POST or None)
	if form.is_valid():
		genero = form.cleaned_data['genero']
		#edadDesde = form.cleaned_data['edadDesde']
		#edadHasta = form.cleaned_data['edadHasta']
		#pais = form.cleaned_data['pais']
		tallaDesde = form.cleaned_data['tallaDesde']
		tallaHasta = form.cleaned_data['tallaHasta']
		pesoDesde = form.cleaned_data['pesoDesde']
		pesoHasta = form.cleaned_data['pesoHasta']
		obesidad = form.cleaned_data['obesidad']
		enfermedad = form.cleaned_data['enfermedad']
		actividadFisica = form.cleaned_data['actividadFisica']
		query = userProfile.objects.all()
		if(genero !='t'):
			query = query.filter(genero=genero)
		if(tallaDesde != 't' or tallaHasta != 't'):	
			if(tallaDesde != 't' and tallaHasta !='t'):
				antropometricos = datosAntropometricos.objects.filter(estatura__range=(tallaDesde,tallaHasta))
			elif(tallaDesde != 't'):
				antropometricos = datosAntropometricos.objects.filter(estatura__gte=tallaDesde)
			elif(tallaHasta != 't'):
				antropometricos = datosAntropometricos.objects.filter(estatura__lte=tallaHasta)	
			id = []
			for item in antropometricos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	
		if(genero !='t'):
			query = query.filter(genero=genero)

		if(pesoDesde != 't' or pesoHasta != 't'):	
			if(pesoDesde != 't' and pesoHasta !='t'):
				antropometricos = datosAntropometricos.objects.filter(peso__range=(pesoDesde,pesoHasta))
			elif(pesoDesde != 't'):
				antropometricos = datosAntropometricos.objects.filter(peso__gte=pesoDesde)
			elif(pesoHasta != 't'):
				antropometricos = datosAntropometricos.objects.filter(peso__lte=pesoHasta)	
			id = []
			for item in antropometricos:
				id.append(item.user_id) 
		if(obesidad != 't'):
			antropometricos = antropometricosResultado.objects.filter(apreciacion_obesidad=obesidad)
			id_antro=[]
			for item in antropometricos:
				id_antro.append(item.datosAntropometricos_id)
			datos = datosAntropometricos.objects.filter(pk__in=id_antro)
			id = []
			for item in datos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	
		if(enfermedad != 't'):
			if(enfermedad == "0"):
				antropometricos = datosAntropometricos.objects.filter(hipertencion=1)			
			elif(enfermedad == "1"):
				antropometricos = datosAntropometricos.objects.filter(diabetes=1)
			elif(enfermedad == "2"):
				antropometricos = datosAntropometricos.objects.filter(cancer=1)
			elif(enfermedad == "3"):
				antropometricos = datosAntropometricos.objects.filter(colesterol=1)
			else:
				antropometricos = datosAntropometricos.objects.filter(trigliceridos=1)
			id = []
			for item in antropometricos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	
		if(actividadFisica != 't'):
			ipaqs = ipaqResultado.objects.filter(apreciacionIpaq=actividadFisica)
			id_ipaq=[]
			for item in ipaqs:
				id_ipaq.append(item.ipaq_id)
			datos = ipaq.objects.filter(pk__in=id_ipaq)
			id = []
			for item in datos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	
	for item in query:
		print item.user_id	
	print query.count()							
	ctx={'form': form,}
	return render_to_response('nutricionista/busqueda.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def perfilUsuarios(request):
	if request.user.has_perm('data.add_alimento') and request.user.has_perm('data.change_alimento'):#BUSCAR COMO VERIFICAR SI ES NUTRICIONISTA
		getUser = request.GET.get('user',1)
		tipoPerfil = request.GET.get('p',0)
		descarga = request.GET.get('d',0)
		nombre = None
		try:
			if getUser > 1:
				if not User.objects.filter(id=getUser):
					return HttpResponseRedirect("/perfiles/")
				if int(tipoPerfil)==1:
					perfil = datosAntropometricos.objects.getByIdJoin(int(getUser))
				elif int(tipoPerfil)==2:
					perfil = ipaqResultado.objects.getResultados(int(getUser))
				elif int(tipoPerfil)==3:
					perfil = frecuenciaConsumo.objects.getDataById(int(getUser))
				elif int(tipoPerfil)==4:
					perfil = None
				elif int(tipoPerfil)==5:
					perfil = indicadoresDieteticos.objects.getById(int(getUser))
				elif int(descarga)>0:
					from xlwt import *
					wb = crear_excel(int(getUser))
					response = HttpResponse(mimetype="application/ms-excel")
					nom = User.objects.filter(id=int(getUser))
					nombreArchivo =nom[0].first_name.capitalize()+nom[0].last_name.capitalize() +"Ipaq.xls"
					response['Content-Disposition'] = 'attachment; filename=' + nombreArchivo
					wb.save(response)
					return response
				else:
					perfil = None
					tipoPerfil = 0
				nombre = User.objects.filter(id=getUser)
				usuario = userProfile.objects.filter(user=getUser)
				#usuario = userProfile.objects.getUserJoin(int(getUser))
			else:
				nombre = User.objects.all()
				usuario = userProfile.objects.all()
				#usuario = userProfile.objects.getAllUser()
				perfil = None
		
		except ValueError:
			return HttpResponseRedirect("/perfiles/")
		#ctx= {'usuario':usuario,'perfil':perfil,'tipo':tipoPerfil, }	
		ctx= {'nombre':nombre,'usuario':usuario,'perfil':perfil,'tipo':tipoPerfil, }	
		return render_to_response('nutricionista/perfilUsuarios.html', ctx, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/profile/")

def crear_excel(id):
	querySetIpaq = list(ipaqResultado.objects.getResultados(id))
	from xlwt import *
	wb = Workbook()
	ws = wb.add_sheet('Sheetname')
	pattern = Pattern()
	pattern.pattern = Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour =22
	style = XFStyle() 
	style.pattern = pattern
	nombres = ["IdentificacionHistoria","TRABAJO","IDIASActivig","ITiempoActivig","ITiempoActivigTRUNK","IDiaActmod","ITiempoActmod","ITiempoActmodTRUNK","IDiaAndar","ITiempoAndar","ITiempoAndarTRUNK","IIViajevehiculo","IITiempoViajaVehi","IIdDiaBicicleta","IITiempoBici","IITiempoBiciTRUNK","IIDiaAndar","IITiempoAndar","IITiempoAndarTRUNK","IIIDiaVigJar","IIITiempoVigJar","IIITiempoVigJarTRUNK","IIIDiaModJar","IIITiempoModJar","IIITiempoModJarTRUNK","IIIDiaModCasa","IIITiempoModCasa","IIITiempoModCasaTRUNK","IVDiasAndar","IVTiempoAndar","	IVTiempoAndarTRUNK","IVDiaVigo","IVTiempoVigo","IVTiempoVigoTRUNK","IVDiaMod","IVTiempoMod","IVTiempoModTRUNK","TiempoSentado","TiempoSentadofindesemana","IAndarMET","IModMet","IVigMet","ITotalMET","IIBiciMET","IIAndarMET","IITotalMET","IIIVigJarMET","IIIModJarMET","IIIModCasaMET","IIITotalMET","IVAndarMET","IVModMET","	IVVigMET","IVTotalMET","METsTotalesAreas","METsAndar","METsMod","METsVig","METsTotalesAct","DiasTAndar","DiasTMod","DiasTVig","TotalDias","MinAndar","MinMod","MinVig","DiasAndarMod","MinAndarMod","Alta","Moderada","Leve","PatronActFisica"]
	i = 0
	for item in nombres:
		ws.write(0,i,item,style)
		ws.col(i).width = 3500
		i += 1
	for item in querySetIpaq:
		lista = [item.id,item.trabaja,item.p2a_trabajo,item.minVigorosoTrabajo,item.minVigorosoTrabajo, \
		item.p4a_trabajo, item.minModeradoTrabajo,item.minModeradoTrabajo,item.p6a_trabajo,item.minAndarTrabajo,\
		item.minModeradoTrabajo,item.p8b_transporte,item.minVehiculo,item.p10a_transporte,item.minModeradoTransporte,\
		item.minModeradoTransporte,item.p12a_transporte, item.minAndarTransporte, item.minAndarTransporte, item.p14a_hogar,\
		item.minVigorosoHogar, item.minVigorosoHogar, item.p16a_hogar, item.minModeradoHogar, item.minModeradoHogar,\
		item.p19a_hogar, item.minModeradoHogar, item.minModeradoHogar, item.p20a_recreacion, item.minAndarRecre, \
		item.minAndarRecre, item.p22a_recreacion, item.minVigorosoRecre, item.minVigorosoRecre, item.p24a_recreacion,\
		item.minModeradoRecre, item.minModeradoRecre, "tiempoSentado","tiempoSentadoFS", item.metAndarTrabajo, \
		item.metModeradoTrabajo, item.metVigorosoTrabajo, item.metTrabajo, item.metModeradoTransporte, item.metAndarTransporte,\
		item. metTransporte, item.metVigorosoHogar, item.metModeradoJHogar, item.metModeradoHogar, item.metHogar,\
		item.metAndarRecreacion, item.metModeradoRecreacion, item.metVigorosoRecreacion, item.metRecreacion, item.metTotal, \
		item.metTotalAndar, item.metTotalModerado, item.metTotalVigoroso, item.metTotal,item.diasTotalAndar, item.diasTotalModerado, \
		item.diasTotalVigoroso, item.diasTotal, item.tiempoAndar, item.tiempoModerado, item.tiempoVigoroso ]
	i=0	
	for item in lista:
		ws.write(1,i,item)
		i += 1
	return wb
