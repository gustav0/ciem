from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile, datosAntropometricos, ipaq, ipaqResultado, antropometricosResultado
from django.contrib.auth.models import User
import math

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
	def cal_metabolismoBasal(self, request):
		id = request.user.id
		#falta edad
		edad = 0
		genero= userProfile.objects.get(user=id).genero
		peso = float(self.cleaned_data["peso"])
		estatura = float(self.cleaned_data["estatura"])	
		if(genero == 'f'):
			MB = 655.1 + (9.6 * peso) + (1.850 * estatura) - (4.676 * edad)
		return MB
	
	def cal_obesidad(self):
		peso = float(self.cleaned_data["peso"])
		estatura = float(self.cleaned_data["estatura"])	
		obesidad = (peso)/(math.pow(estatura,2))
		print obesidad
		return obesidad
		
	def cal_indiceAdiposidad(self):
		circunferencia_cadera = float(self.cleaned_data["circunferencia_cadera"])
		estatura = float(self.cleaned_data["estatura"])
		
	def save(self,request):
		print ("kjjh")
		datosAntropometricos = super(antropometricosForm,self).save()
		antropometricosResultado.objects.create(datosAntropometricos=datosAntropometricos,metabolismoBasal =self.cal_metabolismoBasal(request), obesidad = self.cal_obesidad())
		return datosAntropometricos			
		
class ipaqForm(ModelForm):
	global minAndandoTotal
	global minVigorosoTotal
	global minModeradoTotal
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
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p2a_trabajo"])
		vSino= self.cleaned_data["p2b_trabajo"]
		vHoras= float(self.cleaned_data["p3a_trabajo"])
		vMin= float(self.cleaned_data["p3b_trabajo"])
		mDias= float(self.cleaned_data["p4a_trabajo"])
		mSino= self.cleaned_data["p4b_trabajo"]
		mHoras= float(self.cleaned_data["p5a_trabajo"])
		mMin= float(self.cleaned_data["p5b_trabajo"])
		aDias= float(self.cleaned_data["p6a_trabajo"])
		aSino= self.cleaned_data["p6b_trabajo"]
		aHoras= float(self.cleaned_data["p7a_trabajo"])
		aMin= float(self.cleaned_data["p7b_trabajo"])
		#Calculo los minutos totales
		print vSino
		if(mSino == '1'):
			mMinutos = mMin + (mHoras * 60.0)
			minModeradoTotal = mMinutos
		else:
			mMinutos = 0
			minModeradoTotal = mMinutos
		
		if(aSino== '1'):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal = aMinutos
		else: 
			aMinutos = 0
			minAndandoTotal = aMinutos
		if(vSino== '1'): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal = vMinutos
		else: 
			vMinutos = 0
			minVigorosoTotal = vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		
		#Calculo Total mets en Trabajo
		return (metVigoroso + metModerado + metAndar)
		
	def cal_metTransporte(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
	    # v= vigorosa, m=moderada, a=andar
		mDias= float(self.cleaned_data["p10a_transporte"])
		mSino= self.cleaned_data["p10b_transporte"]
		mHoras= float(self.cleaned_data["p11a_transporte"])
		mMin= float(self.cleaned_data["p11b_transporte"])
		aDias= float(self.cleaned_data["p12a_transporte"])
		aSino= self.cleaned_data["p12b_transporte"]
		aHoras= float(self.cleaned_data["p13a_transporte"])
		aMin= float(self.cleaned_data["p13b_transporte"])
		
		# Caalculo de los minutos totales
		if(mSino == '1'):
			mMinutos = mMin + (mHoras * 60.0)
			minModeradoTotal += mMinutos
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== '1'):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += aMinutos
		else: 
			aMinutos = 0
			minAndandoTotal += aMinutos
		#Caalculo mets para vigoroso, moderado, andar en Trabajo
		metModerado = 6.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		#Calculo Total mets en Trabajo
		total = metModerado + metAndar
		return total
		
	def cal_metHogar(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p14a_hogar"])
		vSino= self.cleaned_data["p14b_hogar"]
		vHoras= float(self.cleaned_data["p15a_hogar"])
		vMin= float(self.cleaned_data["p15b_hogar"])
		mDias= float(self.cleaned_data["p16a_hogar"])
		mSino= self.cleaned_data["p16b_hogar"]
		mHoras= float(self.cleaned_data["p17a_hogar"])
		mMin= float(self.cleaned_data["p17b_hogar"])
		aDias= float(self.cleaned_data["p18a_hogar"])
		aSino= self.cleaned_data["p18b_hogar"]
		aHoras= float(self.cleaned_data["p19a_hogar"])
		aMin= float(self.cleaned_data["p19b_hogar"])
		
		#Calculo los minutos totales
		if(mSino == '1'):
			mMinutos = mMin + (mHoras * 60.0)
			minModeradoTotal += mMinutos
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== '1'):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += aMinutos
		else: 
			aMinutos = 0
			minAndandoTotal += aMinutos
		if(vSino== '1'): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal += vMinutos
		else: 
			vMinutos = 0
			minVigorosoTotal += vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =5.5 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.0 * aMinutos * aDias
		#Calculo Total mets en Trabajo
		return (metVigoroso + metModerado + metAndar)	

	def cal_metRecreacion(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
	    # v= vigorosa, m=moderada, a=andar
		aDias= float(self.cleaned_data["p20a_recreacion"])
		aSino= self.cleaned_data["p20b_recreacion"]
		aHoras= float(self.cleaned_data["p21a_recreacion"])
		aMin= float(self.cleaned_data["p21b_recreacion"])
		vDias= float(self.cleaned_data["p22a_recreacion"])
		vSino= self.cleaned_data["p22b_recreacion"]
		vHoras= float(self.cleaned_data["p23a_recreacion"])
		vMin= float(self.cleaned_data["p23b_recreacion"])
		mDias= float(self.cleaned_data["p24a_recreacion"])
		mSino= self.cleaned_data["p24b_recreacion"]
		mHoras= float(self.cleaned_data["p25a_recreacion"])
		mMin= float(self.cleaned_data["p25b_recreacion"])
		
		#Calculo los minutos totales
		if(mSino == '1'):
			mMinutos = mMin + (mHoras * 60.0)
			minModeradoTotal += mMinutos
		else:
			mMinutos = 0
			minModeradoTotal += mMinutos
		if(aSino== '1'):
			aMinutos = aMin + (aHoras * 60.0)
			minAndandoTotal += aMinutos
		else: 
			aMinutos = float(0)
			minAndandoTotal += aMinutos
		if(vSino== '1'): 
			vMinutos = vMin + (vHoras * 60.0)
			minVigorosoTotal += vMinutos
			print "si"
		else: 
			print "no"
			vMinutos = float(0)
			minVigorosoTotal += vMinutos
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		print vMinutos
		metModerado= 4.0 * mMinutos * mDias
		metAndar = 3.0 * aMinutos * aDias
		#Calculo Total mets en Trabajo
		return (metVigoroso + metModerado + metAndar)	
		
		
	def save(self):
		global minAndandoTotal, minVigorosoTotal, minModeradoTotal
		ipaq = super(ipaqForm,self).save()
		ipaqResultado.objects.create(ipaq=ipaq,metTrabajo=self.cal_metTrabajo(),metTransporte=self.cal_metTransporte(),metHogar=self.cal_metHogar(), metRecreacion=self.cal_metRecreacion(),tiempoAndar = minAndandoTotal, tiempoVigoroso = minVigorosoTotal, tiempoModerado = minModeradoTotal )
		return ipaq
		
