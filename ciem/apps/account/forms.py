from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from ciem.apps.account.models import userProfile
from ciem.apps.account.models import datosAntropometricos, ipaq
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
	p26b_sentado = forms.TypedChoiceField(choices=((0, 'Si'), (1, 'No')), widget=forms.RadioSelect)
	class Meta:
		model = ipaq