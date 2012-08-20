from django import forms

class contactForm(forms.Form):
	email = forms.EmailField()
	tittle = forms.CharField()
	text = forms.CharField( widget=forms.Textarea )

class registerForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

class loginForm(forms.Form):
    email  = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)