from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile
from ciem.apps.account.models import datosAntropometricos

class registerForm(UserCreationForm):
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	fecha_nacimiento = forms.DateField()
	cedula = forms.FloatField()
	
	def save(self, *arg, **kwargs):
		user = super(registerForm, self).save(*arg, **kwargs)
		userProfile.objects.create(user=user, genero=self.cleaned_data['genero'],fecha_nacimiento=fecha_nacimiento, cedula=cedula,)
		return user

class datosAntropometricosForm(ModelForm):
	class Meta:
		model = datosAntropometricos
