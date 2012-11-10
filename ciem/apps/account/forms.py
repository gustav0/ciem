# coding: latin-1
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.forms.formsets import formset_factory
from django.forms import ModelForm
from ciem.apps.account.models import *
from ciem.apps.countries.models import *
from django.contrib.auth.models import User
import math
from datetime import date

class loginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','placeholder': 'Usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class registerForm(UserCreationForm):
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	cedula = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '9999999'}))
	fecha_nacimiento = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.TextInput(attrs={'placeholder': 'dd-mm-aaaa','autocomplete':'off'}))
	first_name = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre',}))
	last_name = forms.CharField(max_length=30, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
	email = forms.EmailField(max_length=75, label='Email',widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	pais = forms.ModelChoiceField(label="País", queryset=Country.objects.all(), widget=forms.Select(attrs={'class':'selector'}))
	venezuela = forms.ModelChoiceField(label='Estado', queryset=VeState.objects.all(), widget=forms.Select(attrs={'class':'selector'}))
	preguntaSecreta = forms.ChoiceField(label="Pregunta secreta", choices=userProfile.PREGUNTA)
	respuestaSecreta = forms.CharField(max_length=70, label='Respuesta Secreta', widget=forms.TextInput(attrs={'placeholder': 'Respuesta secreta','autocomplete':'off'}))
	def save(self, *arg, **kwargs):
		user = super(registerForm, self).save(*arg, **kwargs)
		#if self.cleaned_data["first_name"] != null:
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]
		userProfile.objects.create(user=user, genero=self.cleaned_data['genero'], fecha_nacimiento=self.cleaned_data['fecha_nacimiento'], cedula=self.cleaned_data['cedula'], pais=self.cleaned_data['pais'],\
		municipio=self.cleaned_data['venezuela'],preguntaSecreta=self.cleaned_data['preguntaSecreta'],respuestaSecreta=self.cleaned_data['respuestaSecreta'])
		return user

class recuperarContrasenaForm(forms.Form):
	username = forms.CharField(max_length=70)
	cedula = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '9999999'}))
	respuestaSecreta = forms.CharField(max_length=70, label='Respuesta Secreta', widget=forms.TextInput(attrs={'placeholder': 'Respuesta secreta'}))

class editRegisterForm(ModelForm):
	class Meta:
		model = userProfile

class soyProfesionalForm(ModelForm):
	class Meta:
		model = profesional

class antropometricosForm(ModelForm):
	class Meta:
		model = datosAntropometricos

	def calcular_metabolismoBasal(self, request):
		edad = self.calculate_age(userProfile.objects.get(user_id=request.user.id).fecha_nacimiento)
		genero= userProfile.objects.get(user_id=request.user.id).genero
		peso = float(self.cleaned_data["peso"])
		estatura = float(self.cleaned_data["estatura"])	
		if genero == 'f':
			mb = 655.1 + (9.6 * peso) + (1.850 * estatura) - (4.676 * edad)
		elif genero == 'm':
			mb = 66.4 + (13.75 * peso) + (5.003 * estatura) - (6.775 * edad)
		else:
			mb = 0
		return mb

	
	def calcular_obesidad(self):
		peso = float(self.cleaned_data["peso"])
		estatura = float(self.cleaned_data["estatura"])	
		estaturaFinal = estatura/100
		obesidad = peso / (math.pow(estaturaFinal,2))
		return obesidad	
	def calcular_apreciacion_obesidad(self):
		ob = self.calcular_obesidad()
		if( ob < 24.9):
			apreciacion="Normopeso"
		elif ( ob < 29.9):
			apreciacion="Sobrepeso (Obesidad grado I)" 
		elif ( ob < 34.9 ):
			apreciacion="Obesidad grado II " 	
		elif ( ob < 39.9 ):
			apreciacion="Obesidad grado III " 	
		else:
			apreciacion="Obesidad grado IV" 				
		return apreciacion

	def calcular_indiceAdiposidad(self,request):
		genero= userProfile.objects.get(user_id=request.user.id).genero
		circunferencia_cadera = float(self.cleaned_data["circunferencia_cadera"])
		estatura = float(self.cleaned_data["estatura"])
		estaturaFinal = estatura/100
		ia= (circunferencia_cadera/(estaturaFinal * math.sqrt(estaturaFinal)))-18
		if genero == 'f' or genero == 'o':
			if ia > 35:
				apreciacion_adiposidad = "Aumentado"
			else: 
				apreciacion_adiposidad = "Normal"
		elif genero == 'm':
			if ia > 25:
				apreciacion_adiposidad = "Aumentado"
			else: 
				apreciacion_adiposidad = "Normal"
		else:
			apreciacion_adiposidad =""
		adiposidad = {'indiceAdiposidad':ia, 'apreciacion_adiposidad':apreciacion_adiposidad}
		return adiposidad

	def calcular_cintura(self,request):
		genero= userProfile.objects.get(user_id=request.user.id).genero
		cc = float(self.cleaned_data["circunferencia_cintura"])
		if genero == 'f':
			if cc >= 88:
				apreciacion_cintura = "Signo de Obesidad"
			else: 
				apreciacion_cintura = "Normal"
		elif genero == 'm' or genero == 'o':
			if cc >= 102:
				apreciacion_cintura = "Signo de Obesidad"
			else: 
				apreciacion_cintura  = "Normal"
		else:
			apreciacion_cintura  =""		
		return apreciacion_cintura

	def calculate_age(self,born):
	    today = date.today()
	    try: # raised when birth date is February 29 and the current year is not a leap year
	        birthday = born.replace(year=today.year)
	    except ValueError:
	        birthday = born.replace(year=today.year, day=born.day-1)
	    if birthday > today:
	        return today.year - born.year - 1
	    else:
	        return today.year - born.year
	

	def save(self,request):
		datosAntropometricos = super(antropometricosForm,self).save()
		adiposidad = self.calcular_indiceAdiposidad(request)
		antropometricosResultado.objects.create(datosAntropometricos=datosAntropometricos,metabolismoBasal=self.calcular_metabolismoBasal(request),indiceAdiposidad=adiposidad['indiceAdiposidad'],obesidad = self.calcular_obesidad(),apreciacion_obesidad=self.calcular_apreciacion_obesidad(),apreciacion_adiposidad=adiposidad['apreciacion_adiposidad'],apreciacion_cintura=self.calcular_cintura(request))
		return datosAntropometricos			
	

class recordatorioForm(ModelForm):
	desayuno = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	merienda1 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	almuerzo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	merienda2 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	cena = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	merienda3 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	CHOICES = (('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'))
	diasDesayuno = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	diasMerienda1 = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	diasAlmuerzo = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	diasMerienda2 = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	diasCena = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	diasMerienda3 = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='7')
	valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']
	horaDesayuno =forms.TimeField(help_text='ex: 8:30AM', input_formats=valid_time_formats)
	horaMerienda1 =forms.TimeField(help_text='ex: 10:30AM', input_formats=valid_time_formats)
	horaAlmuerzo =forms.TimeField(help_text='ex: 1:30PM', input_formats=valid_time_formats)
	horaMerienda2 =forms.TimeField(help_text='ex: 3:30PM', input_formats=valid_time_formats)
	horaCena = forms.TimeField(help_text='ex: 6:00PM', input_formats=valid_time_formats)
	horaMerienda3 =forms.TimeField(help_text='ex: 8:00PM', input_formats=valid_time_formats)
	
	class Meta:
		model = datosRecordatorio


class recordatorioAlimentos(ModelForm):
	class Meta:
		model = alimentoRecordatorio
	
class ipaqForm(ModelForm):
	global minAndandoTotal,minVigorosoTotal, minModeradoTotal, metTotal,metTotalVigoroso,metTotalModerado, metTotalAndar
	metTotal = 0.0
	metTotalVigoroso=0.0
	metTotalModerado=0.0
	metTotalAndar=0.0
	p2b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p4b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p6b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p8b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p10b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p12b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p14b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p16b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p18b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p20b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p22b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p24b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)

	class Meta:
		model = ipaq
		
	def cal_metTrabajo(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal, metTotalVigoroso, metTotalModerado, metTotalAndar, diasTotalVigoroso, diasTotalAndar, diasTotalModerado
		#Inicializar total
		trabaja = 0
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p2a_trabajo"])
		vSino= int(self.cleaned_data["p2b_trabajo"])
		vHoras= float(self.cleaned_data["p3a_trabajo"])
		vMin= float(self.cleaned_data["p3b_trabajo"])
		mDias= float(self.cleaned_data["p4a_trabajo"])
		mSino= int(self.cleaned_data["p4b_trabajo"])
		mHoras= float(self.cleaned_data["p5a_trabajo"])
		mMin= float(self.cleaned_data["p5b_trabajo"])
		aDias= float(self.cleaned_data["p6a_trabajo"])
		aSino= int(self.cleaned_data["p6b_trabajo"])
		aHoras= float(self.cleaned_data["p7a_trabajo"])
		aMin= float(self.cleaned_data["p7b_trabajo"])
		#Calculo los minutos totales
		if(mSino == 0):
			mMinutos = mMin + (mHoras * 60.0)
			minModerado = (mMinutos * mDias) 
			minModeradoTotal = minModerado 
			trabaja = 1
			diasTotalModerado = mDias
		else:
			mMinutos = 0
			minModeradoTotal = mMinutos
			minModerado = 0
			diasTotalModerado = 0
		
		if(aSino== 0):
			trabaja = 1
			aMinutos = aMin + (aHoras * 60.0)
			minAndar = (aMinutos * aDias)
			minAndandoTotal = minAndar	
			diasTotalAndar = aDias
		else: 
			aMinutos = 0
			minAndandoTotal = aMinutos
			minAndar = 0
			diasTotalAndar = 0
		if(vSino== 0):
			trabaja = 1 
			vMinutos = vMin + (vHoras * 60.0)
			minVigoroso = (vMinutos * vDias) 
			minVigorosoTotal = minVigoroso
			diasTotalVigoroso = vDias
		else: 
			vMinutos = 0
			minVigorosoTotal = vMinutos
			minVigoroso = 0
			diasTotalVigoroso = 0
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metTotalVigoroso = metVigoroso
		metModerado = 4.0 * mMinutos * mDias
		metTotalModerado = metModerado
		metAndar = 3.3 * aMinutos * aDias
		metTotalAndar = metAndar
		#Calculo Total mets en Trabajo
		metTrabajo = metVigoroso + metModerado + metAndar
		metTotal = metTrabajo
		trabajo = {"trabaja":float(trabaja), "metTrabajo":metTrabajo,"minModerado":minModerado,"minVigoroso":minVigoroso, "minAndar":minAndar, "metVigoroso":metVigoroso,"metModerado":metModerado,"metAndar":metAndar}
		return trabajo
		
	def cal_metTransporte(self):
		global minAndandoTotal, minModeradoTotal, metTotal, metTotalModerado, metTotalAndar, diasTotalAndar, diasTotalModerado
		mDias= float(self.cleaned_data["p10a_transporte"])
		mSino= int(self.cleaned_data["p10b_transporte"])
		mHoras= float(self.cleaned_data["p11a_transporte"])
		mMin= float(self.cleaned_data["p11b_transporte"])
		aDias= float(self.cleaned_data["p12a_transporte"])
		aSino= int(self.cleaned_data["p12b_transporte"])
		aHoras= float(self.cleaned_data["p13a_transporte"])
		aMin= float(self.cleaned_data["p13b_transporte"])
		
		# Caalculo de los minutos totales
		if(mSino == 0):
			mMinutos = mMin + (mHoras * 60.0)
			minModerado = (mMinutos *mDias)
			minModeradoTotal += minModerado
			diasTotalModerado += mDias
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
			minModerado = 0
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndar = (aMinutos * aDias)
			minAndandoTotal += minAndar
			diasTotalAndar += aDias
		else: 
			aMinutos = 0
			minAndandoTotal += aMinutos
			minAndar = 0
		#Caalculo mets para vigoroso, moderado, andar en Trabajo
		metModerado = 6.0 * mMinutos * mDias
		metTotalModerado += metModerado
		metAndar = 3.3 * aMinutos * aDias
		metTotalAndar += metAndar
		#Calculo Total mets en transporte
		metTransporte = metModerado + metAndar
		metTotal +=metTransporte
		transporte = {"metTransporte":metTransporte,"minModerado":minModerado,"minAndar":minAndar,"metModerado":metModerado,"metAndar":metAndar}
		return transporte
		
	def cal_metHogar(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal, metTotalVigoroso, metTotalModerado, metTotalAndar, diasTotalVigoroso, diasTotalAndar, diasTotalModerado
		#Inicializar total
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p14a_hogar"])
		vSino= int(self.cleaned_data["p14b_hogar"])
		vHoras= float(self.cleaned_data["p15a_hogar"])
		vMin= float(self.cleaned_data["p15b_hogar"])
		mDias= float(self.cleaned_data["p16a_hogar"])
		mSino= int(self.cleaned_data["p16b_hogar"])
		mHoras= float(self.cleaned_data["p17a_hogar"])
		mMin= float(self.cleaned_data["p17b_hogar"])
		mjDias= float(self.cleaned_data["p18a_hogar"])
		mjSino= int(self.cleaned_data["p18b_hogar"])
		mjHoras= float(self.cleaned_data["p19a_hogar"])
		mjMin= float(self.cleaned_data["p19b_hogar"])
		
		#Calculo los minutos totales
		if(mSino == 0):
			mMinutos = mMin + (mHoras * 60.0)
			minModerado = (mMinutos * mDias)
			minModeradoTotal += minModerado
			diasTotalModerado += mDias
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
			minModerado = 0
		if(vSino== 0):
			vMinutos = vMin + (vHoras * 60.0)
			minVigoroso =  (vMinutos * vDias)
			minVigorosoTotal += minVigoroso
			diasTotalVigoroso += vDias
		else: 
			vMinutos = 0
			minVigorosoTotal += vMinutos
			minVigoroso = 0
		if(mjSino== 0): 
			mjMinutos = mjMin + (mjHoras * 60.0)
			minModeradoJ = (mjMinutos * mjDias)
			minModeradoTotal += minModeradoJ
			diasTotalModerado += mjDias
		else: 
			mjMinutos = 0
			minModeradoTotal += mjMinutos
			minModeradoJ = 0
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metModeradoJ =5.5 * mjMinutos * mjDias
		metModerado = 4.0 * mMinutos * mDias
		metTotalModerado += (metModerado + metModeradoJ)
		metVigoroso = 3.0 * vMinutos * vDias
		metTotalVigoroso += metVigoroso
		#Calculo Total mets en Hogar
		metHogar = metModeradoJ + metModerado + metVigoroso
		metTotal += metHogar
		hogar = {"metHogar":metHogar,"minModerado":minModerado,"minModeradoJ":minModeradoJ, "minVigoroso":minVigoroso, "metModeradoJ":metModeradoJ,"metModerado":metModerado,"metVigoroso":metVigoroso}
		return hogar
	def cal_metRecreacion(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal, metTotalVigoroso, metTotalModerado, metTotalAndar, diasTotalVigoroso, diasTotalAndar, diasTotalModerado
		#Inicializar total
	    # v= vigorosa, m=moderada, a=andar
		aDias= float(self.cleaned_data["p20a_recreacion"])
		aSino= int(self.cleaned_data["p20b_recreacion"])
		aHoras= float(self.cleaned_data["p21a_recreacion"])
		aMin= float(self.cleaned_data["p21b_recreacion"])
		vDias= float(self.cleaned_data["p22a_recreacion"])
		vSino= int(self.cleaned_data["p22b_recreacion"])
		vHoras= float(self.cleaned_data["p23a_recreacion"])
		vMin= float(self.cleaned_data["p23b_recreacion"])
		mDias= float(self.cleaned_data["p24a_recreacion"])
		mSino= int(self.cleaned_data["p24b_recreacion"])
		mHoras= float(self.cleaned_data["p25a_recreacion"])
		mMin= float(self.cleaned_data["p25b_recreacion"])
		
		#Calculo los minutos totales
		if(mSino == 0):
			mMinutos = mMin + (mHoras * 60.0)
			minModerado = (mMinutos * mDias)
			minModeradoTotal += minModerado
			diasTotalModerado += mDias
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
			minModerado = 0
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndar = (aMinutos * aDias)
			minAndandoTotal += minAndar
			diasTotalAndar += aDias
		else: 
			aMinutos = float(0)
			minAndandoTotal += aMinutos
			minAndar = 0
		if(vSino== 0): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigoroso = (vMinutos * vDias)
			minVigorosoTotal += minVigoroso
			diasTotalVigoroso += vDias
		else: 
			vMinutos = float(0)
			minVigorosoTotal += vMinutos
			minVigoroso = 0
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metTotalVigoroso += metVigoroso
		metModerado= 4.0 * mMinutos * mDias
		metTotalModerado += metModerado
		metAndar = 3.0 * aMinutos * aDias
		metTotalAndar += metAndar
		#Calculo Total mets en recreacion
		metRecreacion = metVigoroso + metModerado + metAndar
		metTotal += metRecreacion
		recreacion = {"metRecreacion":metRecreacion,"minModerado":minModerado,"minVigoroso":minVigoroso, "minAndar":minAndar, "metVigoroso":metVigoroso,"metModerado":metModerado,"metAndar":metAndar}
		return recreacion	

		
	def cal_sentadoTotal(self):
		minutosSemana = float(self.cleaned_data["p26b_sentado"])
		minutosFinSemana= float(self.cleaned_data["p27b_sentado"])
		horasSemana= float(self.cleaned_data["p26a_sentado"])
		horasFinSemana= float(self.cleaned_data["p27a_sentado"])
		minSemanaTotal = minutosSemana + (horasSemana * 60.0)
		minFinSemanaTotal = minutosFinSemana + (horasFinSemana*60.0)
		sentado = (minSemanaTotal *5) + (minFinSemanaTotal*2)
		return sentado

	def cal_tiempoVehiculo(self):
		vSino= int(self.cleaned_data["p8b_transporte"])
		vDias= float(self.cleaned_data["p8a_transporte"])
		vHoras= float(self.cleaned_data["p9a_transporte"])
		vMin= float(self.cleaned_data["p9b_transporte"])
		if(vSino== 0): 
			vMinutos = float((vMin + (vHoras * 60.0)) * vDias)
		else: 
			vMinutos = float(0)
		return vMinutos

	def cal_apreciacion(self,metTotal):
		if(float(metTotal) < 1200):
			return "Baja";
		elif(float(metTotal) < 2000):
			return "Moderada"
		else:
			return "Alta"

	def cal_requerimientoCaloricoDiario(self, id, metTotal):
		genero= userProfile.objects.get(user_id=id).genero
		idAntropometrico = datosAntropometricos.objects.filter(user_id = id)
		antropometricos = list(antropometricosResultado.objects.filter(datosAntropometricos_id=idAntropometrico[len(idAntropometrico)-1].id))
		MB = antropometricos[len(antropometricos)-1].metabolismoBasal
		apreciacion = self.cal_apreciacion(metTotal)
		if(genero == 'f'):
			if(apreciacion == "Baja"):
				requerimiento = MB * 1.50 
			elif(apreciacion == "Moderada"):
				requerimiento = MB * 1.64
			elif(apreciacion == "Alta"):
				requerimiento = MB * 1.90  
			else:
				return 0
		else:
			if(apreciacion == "Baja"):
				requerimiento = MB * 1.60 
			elif(apreciacion == "Moderada"):
				requerimiento = MB * 1.78
			elif(apreciacion == "Alta"):
				requerimiento = MB * 2.1  
			else:
				return 0
		return requerimiento

	def save(self,request):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, diasTotalModerado, diasTotalAndar, diasTotalVigoroso
		mediaSentado=(self.cal_sentadoTotal()/7)
		ipaq = super(ipaqForm,self).save()
		trabajo = self.cal_metTrabajo()
		transporte = self.cal_metTransporte()
		hogar = self.cal_metHogar()
		recreacion = self.cal_metRecreacion()
		ipaqResultado.objects.create(ipaq=ipaq,metTrabajo=trabajo["metTrabajo"], metTransporte=transporte["metTransporte"], \
			metHogar=hogar["metHogar"], metRecreacion=recreacion["metRecreacion"],tiempoAndar = minAndandoTotal, tiempoVigoroso = minVigorosoTotal, \
			tiempoModerado = minModeradoTotal, metTotal = metTotal, tiempoSentado=self.cal_sentadoTotal(),MediaSentado = mediaSentado,\
			metTotalAndar = metTotalAndar, metTotalModerado = metTotalModerado, metTotalVigoroso = metTotalVigoroso, minVigorosoTrabajo = trabajo["minVigoroso"],\
			minAndarTrabajo=trabajo["minAndar"] , minModeradoTrabajo= trabajo["minModerado"], minModeradoTransporte= transporte["minModerado"], \
			minAndarTransporte=transporte["minAndar"], minModeradoJHogar=hogar["minModeradoJ"],minModeradoHogar=hogar["minModerado"],minVigorosoHogar=hogar["minVigoroso"],\
			minVigorosoRecre=recreacion["minVigoroso"],minModeradoRecre=recreacion["minModerado"], minAndarRecre=recreacion["minAndar"], metAndarTrabajo =trabajo["metAndar"],\
			metAndarRecreacion = recreacion["metAndar"], metAndarTransporte = transporte["metAndar"], metVigorosoTrabajo = trabajo["metVigoroso"],metVigorosoHogar = hogar["metVigoroso"],\
			metVigorosoRecreacion = recreacion["metVigoroso"], metModeradoHogar = hogar["metModerado"], metModeradoJHogar = hogar["metModeradoJ"],\
			metModeradoTrabajo = trabajo["metModerado"], metModeradoTransporte = transporte["metModerado"], metModeradoRecreacion = recreacion["metModerado"],\
			diasTotalModerado = diasTotalModerado, diasTotalAndar = diasTotalAndar, diasTotalVigoroso = diasTotalVigoroso, \
			diasTotal = float(diasTotalVigoroso+diasTotalAndar+diasTotalModerado), apreciacionIpaq =self.cal_apreciacion(metTotal), requerimientoCaloricoDiario =self.cal_requerimientoCaloricoDiario(request.user.id, metTotal),\
			trabaja= trabajo["trabaja"], minVehiculo = float(self.cal_tiempoVehiculo()))
		return ipaq


class indicadoresDieteticosForm(ModelForm):
	comeEntreComidas = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	modificadoAlimentacionReciente = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	esAlergicoIntolerante = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	suplementoAlimenticio = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	salComidas = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	tieneDieta = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	consumoVariaEmocion = forms.TypedChoiceField(choices=((1, 'Si'), (0, 'No')), widget=forms.RadioSelect)
	class Meta:
		model = indicadoresDieteticos

class frecuencia7Form(ModelForm):
	p1 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p2 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p3 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p4 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p5 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p6 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p7 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p8 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p9 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p10 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p11 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p12 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p13 = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)

	class Meta:
		model = frecuencia7
