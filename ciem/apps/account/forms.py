from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile
from ciem.apps.account.models import datosAntropometricos
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	cedula = forms.FloatField()
	fecha_nacimiento = forms.DateField(input_formats=['%Y-%m-%d'])
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=75)
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
		
class ipaqForm(forms.Form):
	dias = ( ('0','1'),('1','2'),('2','3'),('3','4'),('4','5'),('5','6'),('6','7'), )
	horas = ( ('0','-'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('10','7+'), )
	minutos = ( ('0','5'),('1','10'),('2','15'),('3','30'),('4','45'), )

	p2a_trabajo = forms.ChoiceField(choices = dias)
	p2b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p3a_trabajo = forms.ChoiceField(choices = horas)
	p3b_trabajo = forms.ChoiceField(choices = minutos)

	p4a_trabajo = forms.ChoiceField(choices = dias)
	p4b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p5a_trabajo = forms.ChoiceField(choices = horas)
	p5b_trabajo = forms.ChoiceField(choices = minutos)	

	p6a_trabajo = forms.ChoiceField(choices = dias)
	p6b_trabajo = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p7a_trabajo = forms.ChoiceField(choices = horas)
	p7b_trabajo = forms.ChoiceField(choices = minutos)
	
	p8a_transporte = forms.ChoiceField(choices = dias)
	p8b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p9a_transporte = forms.ChoiceField(choices = horas)
	p9b_transporte = forms.ChoiceField(choices = minutos)

	p10a_transporte = forms.ChoiceField(choices = dias)
	p10b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p11a_transporte = forms.ChoiceField(choices = horas)
	p11b_transporte = forms.ChoiceField(choices = minutos)	
	
	p12a_transporte = forms.ChoiceField(choices = dias)
	p12b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p13a_transporte = forms.ChoiceField(choices = horas)
	p13b_transporte = forms.ChoiceField(choices = minutos)	
	
	p12a_transporte = forms.ChoiceField(choices = dias)
	p12b_transporte = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p13a_transporte = forms.ChoiceField(choices = horas)
	p13b_transporte = forms.ChoiceField(choices = minutos)	
	
	p14a_hogar = forms.ChoiceField(choices = dias)
	p14b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p15a_hogar = forms.ChoiceField(choices = horas)
	p15b_hogar = forms.ChoiceField(choices = minutos)		
	
	p16a_hogar = forms.ChoiceField(choices = dias)
	p16b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p17a_hogar = forms.ChoiceField(choices = horas)
	p17b_hogar = forms.ChoiceField(choices = minutos)	
	
	p18a_hogar = forms.ChoiceField(choices = dias)
	p18b_hogar = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p19a_hogar = forms.ChoiceField(choices = horas)
	p19b_hogar = forms.ChoiceField(choices = minutos)	
	
	p20a_recreacion = forms.ChoiceField(choices = dias)
	p20b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p21a_recreacion = forms.ChoiceField(choices = horas)
	p21b_recreacion = forms.ChoiceField(choices = minutos)	
	
	p22a_recreacion = forms.ChoiceField(choices = dias)
	p22b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p23a_recreacion = forms.ChoiceField(choices = horas)
	p23b_recreacion = forms.ChoiceField(choices = minutos)		
	
	p24a_recreacion = forms.ChoiceField(choices = dias)
	p24b_recreacion = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p25a_recreacion = forms.ChoiceField(choices = horas)
	p25b_recreacion = forms.ChoiceField(choices = minutos)		
	
	p26a_sentado = forms.ChoiceField(choices = dias)
	p26b_sentado = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	p27a_sentado = forms.ChoiceField(choices = horas)
	p27b_sentado = forms.ChoiceField(choices = minutos)		