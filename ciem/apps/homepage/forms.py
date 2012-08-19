from django import forms

class contactForm(forms.Form):
	email = forms.EmailField()
	tittle = forms.CharField()
	text = forms.CharField( widget=forms.Textarea )