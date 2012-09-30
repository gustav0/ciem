from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile, datosAntropometricos, ipaq, ipaqResultado, antropometricosResultado
from django.contrib.auth.models import User
import math
from datetime import date

class registerForm(UserCreationForm):
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	cedula = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '9999999'}))
	fecha_nacimiento = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.TextInput(attrs={'placeholder': 'dd-mm-aaaa'}))
	first_name = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	last_name = forms.CharField(max_length=30, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))

	def save(self, *arg, **kwargs):
		user = super(registerForm, self).save(*arg, **kwargs)
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]
		userProfile.objects.create(user=user, genero=self.cleaned_data['genero'], fecha_nacimiento=self.cleaned_data['fecha_nacimiento'], cedula=self.cleaned_data['cedula'],)
		return user

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

	def calcular_requerimientoCaloricoDiario(self):
		return 0

	def calcular_indiceAdiposidad(self):
		circunferencia_cadera = float(self.cleaned_data["circunferencia_cadera"])
		estatura = float(self.cleaned_data["estatura"])
		ia= (circunferencia_cadera/estatura * math.sqrt(estatura))-18
		return ia

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
		antropometricosResultado.objects.create(datosAntropometricos=datosAntropometricos,metabolismoBasal=self.calcular_metabolismoBasal(request),requerimientoCaloricoDiario=self.calcular_requerimientoCaloricoDiario(),indiceAdiposidad=self.calcular_indiceAdiposidad(),)
		return datosAntropometricos			
		
class ipaqForm(ModelForm):
	global minAndandoTotal
	global minVigorosoTotal
	global minModeradoTotal
	global metTotal
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
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal
		#Inicializar total
		metTotal = 0.0
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
			minModeradoTotal = (mMinutos * mDias) 
		else:
			mMinutos = 0
			minModeradoTotal = mMinutos
		
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal = (aMinutos * aDias)
			
		else: 
			aMinutos = 0
			minAndandoTotal = aMinutos
		if(vSino== 0): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal = (vMinutos * vDias)
		else: 
			vMinutos = 0
			minVigorosoTotal = vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		
		#Calculo Total mets en Trabajo
		metTrabajo = metVigoroso + metModerado + metAndar
		metTotal = metTrabajo
		return (metTrabajo)
		
	def cal_metTransporte(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal
	    # v= vigorosa, m=moderada, a=andar
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
			minModeradoTotal += (mMinutos *mDias)
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += (aMinutos * aDias)
		else: 
			aMinutos = 0
			minAndandoTotal += aMinutos
		#Caalculo mets para vigoroso, moderado, andar en Trabajo
		metModerado = 6.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		#Calculo Total mets en transporte
		metTransporte = metModerado + metAndar
		metTotal +=metTransporte
		return metTransporte
		
	def cal_metHogar(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p14a_hogar"])
		vSino= int(self.cleaned_data["p14b_hogar"])
		vHoras= float(self.cleaned_data["p15a_hogar"])
		vMin= float(self.cleaned_data["p15b_hogar"])
		mDias= float(self.cleaned_data["p16a_hogar"])
		mSino= int(self.cleaned_data["p16b_hogar"])
		mHoras= float(self.cleaned_data["p17a_hogar"])
		mMin= float(self.cleaned_data["p17b_hogar"])
		aDias= float(self.cleaned_data["p18a_hogar"])
		aSino= int(self.cleaned_data["p18b_hogar"])
		aHoras= float(self.cleaned_data["p19a_hogar"])
		aMin= float(self.cleaned_data["p19b_hogar"])
		
		#Calculo los minutos totales
		if(mSino == 0):
			mMinutos = mMin + (mHoras * 60.0)
			minModeradoTotal += (mMinutos * mDias)
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += (aMinutos * aDias)
		else: 
			aMinutos = 0
			minAndandoTotal += aMinutos
		if(vSino== 0): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal += (vMinutos * vDias)
		else: 
			vMinutos = 0
			minVigorosoTotal += vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =5.5 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.0 * aMinutos * aDias
		#Calculo Total mets en Hogar
		metHogar = metVigoroso + metModerado + metAndar
		metTotal += metHogar
		return (metHogar)	

	def cal_metRecreacion(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal, metTotal
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
			minModeradoTotal += (mMinutos * mDias)
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== 0):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += (aMinutos * aDias)
		else: 
			aMinutos = float(0)
			minAndandoTotal += aMinutos
		if(vSino== 0): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal += (vMinutos * vDias)
		else: 
			vMinutos = float(0)
			minVigorosoTotal += vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metModerado= 4.0 * mMinutos * mDias
		metAndar = 3.0 * aMinutos * aDias
		#Calculo Total mets en recreacion
		metRecreacion = metVigoroso + metModerado + metAndar
		metTotal += metRecreacion
		return (metRecreacion)	
		
	def cal_sentadoTotal(self):
		minutosSemana = float(self.cleaned_data["p26b_sentado"])
		minutosFinSemana= float(self.cleaned_data["p27b_sentado"])
		horasSemana= float(self.cleaned_data["p26a_sentado"])
		horasFinSemana= float(self.cleaned_data["p27a_sentado"])
		minSemanaTotal = minutosSemana + (horasSemana * 60.0)
		minFinSemanaTotal = minutosFinSemana + (horasFinSemana*60.0)
		sentado = (minSemanaTotal *5) + (minFinSemanaTotal*2)
		return sentado

		
	def save(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
		mediaSentado=(self.cal_sentadoTotal()/7)
		ipaq = super(ipaqForm,self).save()
		ipaqResultado.objects.create(ipaq=ipaq,metTrabajo=self.cal_metTrabajo(),metTransporte=self.cal_metTransporte(),metHogar=self.cal_metHogar(), metRecreacion=self.cal_metRecreacion(),tiempoAndar = minAndandoTotal, tiempoVigoroso = minVigorosoTotal, tiempoModerado = minModeradoTotal, metTotal = metTotal, tiempoSentado=self.cal_sentadoTotal(),MediaSentado = mediaSentado)
		return ipaq
		
