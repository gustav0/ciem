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
	dias = (
	('1','1 dia'),
	('2','2 dias'),
	('3','3 dias'),
	('4','4 dias'),
	('5','5 dias'),
	)
	
	horas = (
	('0','Menos de 1 hora'),
	('1','1 hora'),
	('2','2 horas'),
	('3','3 horas'),
	('4','4 horas'),
	('5','5 horas'),
	('6','6 horas'),
	('10','Mas de 6 horas'),	
	)	
	p2a_trabajo = forms.ChoiceField(choices = dias)
	p2b_trabajo = boolfield = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
                   choices=((0, 'Si'), (1, 'No')),
                   widget=forms.RadioSelect
                )
	p3a_trabajo = forms.ChoiceField(choices = horas)
	p3b_trabajo = forms.FloatField()
	p4a_trabajo = forms.ChoiceField(choices = dias)
	p4b_trabajo = forms.BooleanField()
	p5a_trabajo = forms.ChoiceField(choices = dias)
	p5b_trabajo = forms.FloatField()	
	p6a_trabajo = forms.ChoiceField(choices = dias)
	p6b_trabajo = forms.BooleanField()
	p7a_trabajo = forms.ChoiceField(choices = dias)
	p7b_trabajo = forms.FloatField()