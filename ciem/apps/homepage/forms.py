#!/usr/local/bin/python
# coding: latin-1
from django import forms

class contactForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}))
	asunto = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Escriba el motivo'}))
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
