#!/usr/local/bin/python
# coding: latin-1
from django import forms

class contactForm(forms.Form):
	email = forms.EmailField()
	asunto = forms.CharField()
	texto = forms.CharField( widget=forms.Textarea )

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) <3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) <4:
			raise forms.ValidationError("*")
		return texto
		
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
	)	
	p2a_trabajo = forms.ChoiceField(choices = dias)
	p2b_trabajo = forms.BooleanFiel()
	p3a_trabajo = forms.ChoiceField(choices = horas)
	p3b_trabajo = forms.FloatField(default = 0)
	p4a_trabajo = forms.ChoiceField(choices = dias)
	p4b_trabajo = forms.BooleanFiel()
	p5a_trabajo = forms.ChoiceField(choices = dias)
	p5b_trabajo = forms.FloatField(default = 0)	
	p6a_trabajo = forms.ChoiceField(choices = dias)
	p6b_trabajo = forms.BooleanFiel()
	p7a_trabajo = forms.ChoiceField(choices = dias)
	p7b_trabajo = forms.FloatField(default = 0)
	
	class historiaForm(forms.Form):
	frecuencia = (
		('0','Nunca'),
		('1','1 vez al mes'),
		('2','2 - 3 veces al mes'),
		('3','1 por semana'),
		('4','2 por semana'),
		('5','3 - 4 por semana'),
		('6','5 - 6 por semana'),
		('7','1 vez por dia'),
		('8','2 o mas por dia'),
	)
	tamano = (
		('p','Pequena'),
		('m','Mediana'),
		('g','Grande'),
	)
	f1 = forms.ChoiceField(choices = frecuencia)
	f2 = forms.ChoiceField(choices = frecuencia)
	f3 = forms.ChoiceField(choices = frecuencia)
	f4 = forms.ChoiceField(choices = frecuencia)
	f5 = forms.ChoiceField(choices = frecuencia)
	f6 = forms.ChoiceField(choices = frecuencia)
	f7 = forms.ChoiceField(choices = frecuencia)
	t1 = forms.ChoiceField(choices = tamano)
	t2 = forms.ChoiceField(choices = tamano)
	t3 = forms.ChoiceField(choices = tamano)
	t4 = forms.ChoiceField(choices = tamano)
	t5 = forms.ChoiceField(choices = tamano)
	t6 = forms.ChoiceField(choices = tamano)
	t7 = forms.ChoiceField(choices = tamano)	