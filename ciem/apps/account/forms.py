from django.contrib.auth.forms import UserCreationForm
from django import forms
from ciem.apps.account.models import userProfile

class registerForm(UserCreationForm):
	gender = forms.ChoiceField(choices=userProfile.GENDER)
	def save(self, *arg, **kwargs):
		user = super(registerForm, self).save(*arg, **kwargs)
		userProfile.objects.create(user=user, gender=self.cleaned_data['gender'])
		return user
