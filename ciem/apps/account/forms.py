from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile
from ciem.apps.account.models import datosAntropometricos

class registerForm(UserCreationForm):
	
	genero = forms.ChoiceField(choices=userProfile.GENERO)
	cedula = forms.FloatField()
	fecha_nacimiento = forms.DateField(input_formats=['%Y-%m-%d'])

	def save(self, *arg, **kwargs):
		user = super(registerForm, self).save(*arg, **kwargs)
		userProfile.objects.create(user=user, genero=self.cleaned_data['genero'], fecha_nacimiento=self.cleaned_data['fecha_nacimiento'], cedula=self.cleaned_data['cedula'],)
		return user

class antropometricosForm(ModelForm):
	class Meta:
		model = datosAntropometricos