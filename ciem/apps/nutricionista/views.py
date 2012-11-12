from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger
from ciem.apps.account.models import datosAntropometricos,antropometricosResultado,userProfile,ipaqResultado,ipaq,frecuenciaConsumo, profesional, indicadoresDieteticos
from django.contrib.auth.models import User, Group
from ciem.apps.nutricionista.forms import *
from time import gmtime, strftime

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

@login_required(login_url='/login')
@user_passes_test(lambda u: u.groups.filter(name='profesional').count() == 1 or u.groups.filter(name='profesional2').count() == 1 or u.is_superuser, login_url='/perfil/')
def busqueda(request):
	bandera=False
	d = request.GET.get('d','0')
	form = busquedaForm(request.POST or None)
	query = userProfile.objects.all()
	antropometricoPerfil = datosAntropometricos.objects.all()
	if form.is_valid():
		bandera = True
		cuenta = 0
		genero = form.cleaned_data['genero']
		edadDesde = form.cleaned_data['edadDesde']
		edadHasta = form.cleaned_data['edadHasta']
		pais = form.cleaned_data['pais']
		tallaDesde = form.cleaned_data['tallaDesde']
		tallaHasta = form.cleaned_data['tallaHasta']
		pesoDesde = form.cleaned_data['pesoDesde']
		pesoHasta = form.cleaned_data['pesoHasta']
		obesidad = form.cleaned_data['obesidad']
		hipertencion = form.cleaned_data['enf_hip']
		diabetes = form.cleaned_data['enf_dia']
		cancer = form.cleaned_data['enf_can']
		colesterol = form.cleaned_data['enf_col']
		trigliceridos = form.cleaned_data['enf_tri']
		actividadFisica = form.cleaned_data['actividadFisica']
		currentYear =  strftime("%Y", gmtime())
		currentDay =  strftime("%d", gmtime())
		currentMonth =  strftime("%m", gmtime())
		# BUSQUEDA POR GENERO
		if(genero !='t'):
			query = query.filter(genero=genero)

		# BUSQUEDA POR PAIS
		if(pais):
			query = query.filter(pais=pais)		
		#BUSQUEDA POR EDAD
		if(edadDesde != 't'):
			yearHasta = int(currentYear)-int(edadDesde)
		if(edadHasta != 't'):
			yearDesde = int(currentYear)-int(edadHasta)
		if(edadDesde != 't' or edadHasta != 't'):	
			if(edadDesde != 't' and edadHasta !='t'):
				query = query.filter(fecha_nacimiento__range=(datetime.date(yearDesde, 1, 1),datetime.date(yearHasta, int(currentMonth), int(currentDay))))	
			elif(edadDesde != 't'):
				query = query.filter(fecha_nacimiento__lte=(datetime.date(yearHasta, int(currentMonth), int(currentDay))))	
			elif(edadHasta != 't'):
				query = query.filter(fecha_nacimiento__gte=(datetime.date(yearDesde, 1, 1)))
	
		# BUSQUEDA POR TALLA
		if(tallaDesde != 't' or tallaHasta != 't'):	
			if(tallaDesde != 't' and tallaHasta !='t'):
				antropometricos = datosAntropometricos.objects.filter(estatura__range=(tallaDesde,tallaHasta))
				antropometricoPerfil = datosAntropometricos.objects.filter(estatura__range=(tallaDesde,tallaHasta))	
			elif(tallaDesde != 't'):
				antropometricos = datosAntropometricos.objects.filter(estatura__gte=tallaDesde)
				antropometricoPerfil= datosAntropometricos.objects.filter(estatura__gte=tallaDesde)
			elif(tallaHasta != 't'):
				antropometricos = datosAntropometricos.objects.filter(estatura__lte=tallaHasta)	
				antropometricoPerfil= datosAntropometricos.objects.filter(estatura__lte=tallaHasta)	
			id = []
			for item in antropometricos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	

		# BUSQUEDA POR PESO
		if(pesoDesde != 't' or pesoHasta != 't'):	
			if(pesoDesde != 't' and pesoHasta !='t'):
				antropometricos = datosAntropometricos.objects.filter(peso__range=(pesoDesde,pesoHasta))
				antropometricoPerfil = antropometricoPerfil.filter(peso__range=(pesoDesde,pesoHasta))
			elif(pesoDesde != 't'):
				antropometricos = datosAntropometricos.objects.filter(peso__gte=pesoDesde)
				antropometricoPerfil = antropometricos.filter(peso__gte=pesoDesde)
			elif(pesoHasta != 't'):
				antropometricos = datosAntropometricos.objects.filter(peso__lte=pesoHasta)
				antropometricoPerfil = antropometricos.filter(peso__lte=pesoHasta)
			id = []
			for item in antropometricos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	

		# BUSQUEDA POR OBESIDAD
		if(obesidad != 't'):
			antropometricos = antropometricosResultado.objects.filter(apreciacion_obesidad=obesidad)
			id_antro=[]
			for item in antropometricos:
				id_antro.append(item.datosAntropometricos_id)
			datos = datosAntropometricos.objects.filter(pk__in=id_antro)
			antropometricoPerfil = antropometricoPerfil.filter(pk__in=id_antro)
			id = []
			for item in datos:
				id.append(item.user_id) 
			query = query.filter(pk__in=id)	

		# BUSQUEDA POR PATOLOGIA
		if(hipertencion):
			antropometricos = datosAntropometricos.objects.filter(hipertencion=1)
			antropometricoPerfil = antropometricoPerfil.filter(hipertencion=1)
			query = queryAntro(antropometricos,query)							
		if(diabetes):
			antropometricos = datosAntropometricos.objects.filter(diabetes=1)
			antropometricoPerfil = antropometricoPerfil.filter(diabetes=1)
			query = queryAntro(antropometricos,query)	
		if(cancer):
			antropometricos = datosAntropometricos.objects.filter(cancer=1)
			antropometricoPerfil = antropometricoPerfil.filter(cancer=1)
			query = queryAntro(antropometricos,query)				
		if(colesterol):
			antropometricos = datosAntropometricos.objects.filter(colesterol=1)
			antropometricoPerfil = antropometricoPerfil.filter(colesterol=1)
			query = queryAntro(antropometricos,query)				
		if(trigliceridos):
			antropometricos = datosAntropometricos.objects.filter(trigliceridos=1)
			antropometricoPerfil = antropometricoPerfil.filter(trigliceridos=1)
			query = queryAntro(antropometricos,query)

		# BUSQUEDA POR ACTIVIDAD FISICA	
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
		id_final = []			
		for item in query:
			id_final.append(item.user_id)
		id_antro = []	
		for per in antropometricoPerfil:
			id_antro.append(per.id)
		# COUNTS	
		querySetAntropometrico = datosAntropometricos.objects.filter(user_id__in=id_final, pk__in=id_antro)
		#print "CUENTA ANTRO" 
	#	print querySetAntropometrico.count()	
	cuenta = query.count()
	request.session['userQuery'] = list(query)
	if(d!='0'):
		from xlwt import *
		if d == '1':
			wb = descargarAntropometrico(querySetAntropometrico)
			nombreArchivo ="Antropometrico.xls"	
		elif d == '2':
			wb = descargarIpaq(id_final, actividadFisica)
			nombreArchivo ="Ipaq.xls"		
		#elif d == '3':
		#	wb = descargarAntropometrico(query)										
		response = HttpResponse(mimetype="application/ms-excel")
		response['Content-Disposition'] = 'attachment; filename=' + nombreArchivo
		wb.save(response)
		return response							
	ctx={'form': form,'bandera':bandera, 'cuenta':cuenta}
	return render_to_response('nutricionista/busqueda.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
@user_passes_test(lambda u: u.groups.filter(name='profesional').count() == 1 or u.groups.filter(name='profesional2').count() == 1 or u.is_superuser, login_url='/perfil/')
def perfilUsuarios(request):
	getUser = request.GET.get('user')
	tipoPerfil = request.GET.get('p',0)
	descarga = request.GET.get('d',0)
	nombre = None
	try:
		if getUser > 1:
			if not User.objects.filter(id=getUser):
				return HttpResponseRedirect("/perfiles/")
			if int(tipoPerfil)==1:#datos antropometricos
				perfil = datosAntropometricos.objects.getByIdJoin(int(getUser))
			elif int(tipoPerfil)==2:#resultados del ipaq
				perfil = ipaqResultado.objects.getResultados(int(getUser))
			elif int(tipoPerfil)==3:#frecuenciadeconsumo
				perfil = frecuenciaConsumo.objects.getDataById(int(getUser))
			elif int(tipoPerfil)==4:#recordatorio24
				perfil = None
			elif int(tipoPerfil)==5:#indicadores dieteticos
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
		else:
			if 'userQuery' in request.session:
				userQuery = request.session['userQuery']
				id_user_busqueda = []
				for item in userQuery:
					id_user_busqueda.append(item.id)
				nombre = User.objects.filter(pk__in=id_user_busqueda)
				usuario = userProfile.objects.filter(user_id__in=id_user_busqueda)
				perfil = None
				del request.session['userQuery']
			else:
				nombre = User.objects.all()
				usuario = userProfile.objects.all()
				perfil = None
	except ValueError:
		return HttpResponseRedirect("/perfiles/")
	ctx= {'nombre':nombre,'usuario':usuario,'perfil':perfil,'tipo':tipoPerfil, }	
	return render_to_response('nutricionista/perfilUsuarios.html', ctx, context_instance=RequestContext(request))

def crear_excel(id):
	querySetIpaq = list(ipaqResultado.objects.getResultados(id))
	from xlwt import *
	wb = Workbook()
	ws = wb.add_sheet('IPAQ')
	pattern = Pattern()
	pattern.pattern = Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour =22
	style = XFStyle() 
	style.pattern = pattern
	nombres = ["IdentificacionHistoria","Fecha de creacion","TRABAJO","IDIASActivig","ITiempoActivig","ITiempoActivigTRUNK","IDiaActmod","ITiempoActmod","ITiempoActmodTRUNK","IDiaAndar","ITiempoAndar","ITiempoAndarTRUNK","IIViajevehiculo","IITiempoViajaVehi","IIdDiaBicicleta","IITiempoBici","IITiempoBiciTRUNK","IIDiaAndar","IITiempoAndar","IITiempoAndarTRUNK","IIIDiaVigJar","IIITiempoVigJar","IIITiempoVigJarTRUNK","IIIDiaModJar","IIITiempoModJar","IIITiempoModJarTRUNK","IIIDiaModCasa","IIITiempoModCasa","IIITiempoModCasaTRUNK","IVDiasAndar","IVTiempoAndar","	IVTiempoAndarTRUNK","IVDiaVigo","IVTiempoVigo","IVTiempoVigoTRUNK","IVDiaMod","IVTiempoMod","IVTiempoModTRUNK","TiempoSentado","TiempoSentadofindesemana","IAndarMET","IModMet","IVigMet","ITotalMET","IIBiciMET","IIAndarMET","IITotalMET","IIIVigJarMET","IIIModJarMET","IIIModCasaMET","IIITotalMET","IVAndarMET","IVModMET","	IVVigMET","IVTotalMET","METsTotalesAreas","METsAndar","METsMod","METsVig","METsTotalesAct","DiasTAndar","DiasTMod","DiasTVig","TotalDias","MinAndar","MinMod","MinVig","DiasAndarMod","MinAndarMod","Alta","Moderada","Leve","PatronActFisica"]
	i = 0
	for item in nombres:
		ws.write(0,i,item,style)
		ws.col(i).width = 3500
		i += 1
	j=1	
	for item in querySetIpaq:
		lista = [item.id,str(item.fecha_creacion),item.trabaja,item.p2a_trabajo,item.minVigorosoTrabajo,item.minVigorosoTrabajo, \
		item.p4a_trabajo, item.minModeradoTrabajo,item.minModeradoTrabajo,item.p6a_trabajo,item.minAndarTrabajo,\
		item.minModeradoTrabajo,item.p8b_transporte,item.minVehiculo,item.p10a_transporte,item.minModeradoTransporte,\
		item.minModeradoTransporte,item.p12a_transporte, item.minAndarTransporte, item.minAndarTransporte, item.p14a_hogar,\
		item.minVigorosoHogar, item.minVigorosoHogar, item.p16a_hogar, item.minModeradoHogar, item.minModeradoHogar,\
		item.p19a_hogar, item.minModeradoHogar, item.minModeradoHogar, item.p20a_recreacion, item.minAndarRecre, \
		item.minAndarRecre, item.p22a_recreacion, item.minVigorosoRecre, item.minVigorosoRecre, item.p24a_recreacion,\
		item.minModeradoRecre, item.minModeradoRecre, item.tiempoSentado,item.MediaSentado, item.metAndarTrabajo, \
		item.metModeradoTrabajo, item.metVigorosoTrabajo, item.metTrabajo, item.metModeradoTransporte, item.metAndarTransporte,\
		item. metTransporte, item.metVigorosoHogar, item.metModeradoJHogar, item.metModeradoHogar, item.metHogar,\
		item.metAndarRecreacion, item.metModeradoRecreacion, item.metVigorosoRecreacion, item.metRecreacion, item.metTotal, \
		item.metTotalAndar, item.metTotalModerado, item.metTotalVigoroso, item.metTotal,item.diasTotalAndar, item.diasTotalModerado, \
		item.diasTotalVigoroso, item.diasTotal, item.tiempoAndar, item.tiempoModerado, item.tiempoVigoroso," "," "," ",item.apreciacionIpaq ]
		i=0	
		for item in lista:
			ws.write(j,i,item)
			i += 1
		j+=1	
	return wb

def descargarAntropometrico(querySetAntropometrico):
	from xlwt import *
	wb = Workbook()
	ws = wb.add_sheet('Antropometrico')
	pattern = Pattern()
	pattern.pattern = Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour =22
	style = XFStyle() 
	style.pattern = pattern
	nombres = ["FECHA CREACION","ID USUARIO","NOMBRE","APELLIDO","PESO",\
	"CIRCUNFERENCIA CINTURA","CIRCUNFERENCIA CADERA","ESTATURA","HIPERTENCION",\
	"DIABETES","CANCER","COLESTEROL","TRIGLICERIDOS","METABOLISMO BASAL",\
	"INDICE ADIPOSIDAD","APRECIACION ADIPOSIDAD","OBESIDAD","APRECIACION OBESIDAD",\
	"APRECIACION CINTURA"]
	i = 0
	for item in nombres:
		ws.write(0,i,item,style)
		ws.col(i).width = 3500
		i += 1
	j=1	
	for antro in querySetAntropometrico:
		usuario = User.objects.get(pk=antro.user_id)
		resultados = antropometricosResultado.objects.get(datosAntropometricos_id=antro.id)
		lista = [str(antro.fecha_creacion),antro.user_id,usuario.first_name,usuario.last_name,antro.peso,antro.circunferencia_cintura,\
		antro.circunferencia_cadera,antro.estatura,antro.hipertencion,antro.diabetes,antro.cancer,antro.colesterol,antro.trigliceridos,\
		resultados.metabolismoBasal, resultados.indiceAdiposidad,resultados.apreciacion_adiposidad, \
		resultados.obesidad,resultados.apreciacion_obesidad, resultados.apreciacion_cintura]
		i=0
		for item in lista:
			ws.write(j,i,item)
			i += 1
		j+=1
	return wb

def descargarIpaq(id_usuarios, actividadFisica):
	querySetIpaq = ipaq.objects.filter(user_id__in=id_usuarios)
	from xlwt import *
	wb = Workbook()
	ws = wb.add_sheet('Ipaq')
	pattern = Pattern()
	pattern.pattern = Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour =22
	style = XFStyle() 
	style.pattern = pattern
	nombres = ["FECHA CREACION","ID USUARIO","NOMBRE","APELLIDO","IDIASActivig","ITiempoActivig","ITiempoActivigTRUNK","IDiaActmod","ITiempoActmod","ITiempoActmodTRUNK","IDiaAndar","ITiempoAndar","ITiempoAndarTRUNK","IIViajevehiculo","IITiempoViajaVehi","IIdDiaBicicleta","IITiempoBici","IITiempoBiciTRUNK","IIDiaAndar","IITiempoAndar","IITiempoAndarTRUNK","IIIDiaVigJar","IIITiempoVigJar","IIITiempoVigJarTRUNK","IIIDiaModJar","IIITiempoModJar","IIITiempoModJarTRUNK","IIIDiaModCasa","IIITiempoModCasa","IIITiempoModCasaTRUNK","IVDiasAndar","IVTiempoAndar","	IVTiempoAndarTRUNK","IVDiaVigo","IVTiempoVigo","IVTiempoVigoTRUNK","IVDiaMod","IVTiempoMod","IVTiempoModTRUNK","TiempoSentado","TiempoSentadofindesemana","IAndarMET","IModMet","IVigMet","ITotalMET","IIBiciMET","IIAndarMET","IITotalMET","IIIVigJarMET","IIIModJarMET","IIIModCasaMET","IIITotalMET","IVAndarMET","IVModMET","	IVVigMET","IVTotalMET","METsTotalesAreas","METsAndar","METsMod","METsVig","METsTotalesAct","DiasTAndar","DiasTMod","DiasTVig","TotalDias","MinAndar","MinMod","MinVig","DiasAndarMod","MinAndarMod","Alta","Moderada","Leve","PatronActFisica"]
	i = 0
	for item in nombres:
		ws.write(0,i,item,style)
		ws.col(i).width = 3500
		i += 1
	j=1	
	for ipq in querySetIpaq:
		usuario = User.objects.get(pk=ipq.user_id)
		try:
			if actividadFisica == 't':
				item = ipaqResultado.objects.get(ipaq_id=ipq.id)
			else:
				item = ipaqResultado.objects.get(ipaq_id=ipq.id, apreciacionIpaq=actividadFisica)
			lista = [ipq.fecha_creacion,ipq.user_id,usuario.first_name,usuario.last_name,item.id,item.trabaja,ipq.p2a_trabajo,item.minVigorosoTrabajo,item.minVigorosoTrabajo, \
			ipq.p4a_trabajo, item.minModeradoTrabajo,item.minModeradoTrabajo,ipq.p6a_trabajo,item.minAndarTrabajo,\
			item.minModeradoTrabajo,ipq.p8b_transporte,item.minVehiculo,ipq.p10a_transporte,item.minModeradoTransporte,\
			item.minModeradoTransporte,ipq.p12a_transporte, item.minAndarTransporte, item.minAndarTransporte, ipq.p14a_hogar,\
			item.minVigorosoHogar, item.minVigorosoHogar, ipq.p16a_hogar, item.minModeradoHogar, item.minModeradoHogar,\
			ipq.p19a_hogar, item.minModeradoHogar, item.minModeradoHogar, ipq.p20a_recreacion, item.minAndarRecre, \
			item.minAndarRecre, ipq.p22a_recreacion, item.minVigorosoRecre, item.minVigorosoRecre, ipq.p24a_recreacion,\
			item.minModeradoRecre, item.minModeradoRecre, item.tiempoSentado,item.MediaSentado, item.metAndarTrabajo, \
			item.metModeradoTrabajo, item.metVigorosoTrabajo, item.metTrabajo, item.metModeradoTransporte, item.metAndarTransporte,\
			item. metTransporte, item.metVigorosoHogar, item.metModeradoJHogar, item.metModeradoHogar, item.metHogar,\
			item.metAndarRecreacion, item.metModeradoRecreacion, item.metVigorosoRecreacion, item.metRecreacion, item.metTotal, \
			item.metTotalAndar, item.metTotalModerado, item.metTotalVigoroso, item.metTotal,item.diasTotalAndar, item.diasTotalModerado, \
			item.diasTotalVigoroso, item.diasTotal, item.tiempoAndar, item.tiempoModerado, item.tiempoVigoroso, " "," "," ",item.apreciacionIpaq]
			i=0
			for item in lista:
				ws.write(j,i,item)
				i += 1
			j+=1
		except:
			j=j	
	return wb

def queryAntro(antropometricos,query):
	id = []
	for item in antropometricos:
		id.append(item.user_id) 
	return query.filter(pk__in=id)	
