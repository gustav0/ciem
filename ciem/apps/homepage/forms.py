from django import forms

class contactForm(forms.Form):
	email = forms.EmailField()
	title = forms.CharField()
	text = forms.CharField( widget=forms.Textarea )

	def clean_title(self):
		cd = self.cleaned_data
		title = cd.get('title')
		if len(title) <3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return title

	def clean_text(self):
		cd = self.cleaned_data
		text = cd.get('text')
		if len(text) <10:
			raise forms.ValidationError("Ingrese mas texto")
		return text
	def clean(self):
		cd = self.cleaned_data
		email = cd.get('email')
		title = cd.get('title')
		text = cd.get('text')
		if email == title:
			raise forms.ValidationError("El email no puede ir en el titulo")

		return cd
#class registerForm(forms.Form):
#	email = forms.EmailField()
#	password = forms.CharField(widget=forms.PasswordInput)
#
#class loginForm(forms.Form):
#    email  = forms.EmailField()
#    password = forms.CharField(widget=forms.PasswordInput)