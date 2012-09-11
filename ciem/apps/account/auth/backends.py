from django.contrib.auth.backends import ModelBackend

class loginBackend(ModelBackend):

	def authenticate(Self, username, password):
		return super(loginBackend, Self).authenticate(username,password)