from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile, datosAntropometricos, ipaq, ipaqResultado
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	cedula = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '9999999'}))
	fecha_nacimiento = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'aaaa-mm-dd'}))
	first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
	email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	class Meta:
		model = User
		fields = ("first_name", "last_name", "email",)

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
		
class ipaqForm(ModelForm):
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
		if(vSino==1): vMinutos = vMin + (vHoras * 60.0)
		else: vMinutos = 0
		if(mSino==1): mMinutos = mMin + (mHoras * 60.0)
		else: mMinutos = 0
		if(aSino==1): aMinutos = aMin + (aHoras * 60.0)
		else: aMinutos = 0
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		#Calculo Total mets en Trabajo
		return (metVigoroso + metModerado + metAndar)
		
	def cal_metTransporte(self):
	    # v= vigorosa, m=moderada, a=andar
		vDias= float(self.cleaned_data["p8a_Transporte"])
		vSino= self.cleaned_data["p8b_Transporte"]
		vHoras= float(self.cleaned_data["p9a_Transporte"])
		vMin= float(self.cleaned_data["p9b_Transporte"])
		mDias= float(self.cleaned_data["p10a_Transporte"])
		mSino= self.cleaned_data["p10b_Transporte"]
		mHoras= float(self.cleaned_data["p11a_Transporte"])
		mMin= float(self.cleaned_data["p11b_Transporte"])
		aDias= float(self.cleaned_data["p12a_Transporte"])
		aSino= self.cleaned_data["p12b_Transporte"]
		aHoras= float(self.cleaned_data["p13a_Transporte"])
		aMin= float(self.cleaned_data["p13b_Transporte"])
		
		#Calculo de los minutos totales
		if(vSino==1): vMinutos = vMin + (vHoras * 60.0)
		else: vMinutos = 0
		if(mSino==1): mMinutos = mMin + (mHoras * 60.0)
		else: mMinutos = 0
		if(aSino==1): aMinutos = aMin + (aHoras * 60.0)
		else: aMinutos = 0
		#Calculo mets para vigoroso, moderado, andar en Trabajo
		metVigoroso =8.0 * vMinutos * vDias
		metModerado = 4.0 * mMinutos * mDias
		metAndar = 3.3 * aMinutos * aDias
		#Calculo Total mets en Trabajo
		return (metVigoroso + metModerado + metAndar)	
		
	def save(self):
		ipaq = super(ipaqForm,self).save()
		ipaqResultado.objects.create(ipaq=ipaq,metTrabajo=self.cal_metTrabajo())
		return ipaq
		
