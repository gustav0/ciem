from django.db import models
from django.contrib.auth.models import User
#from ciem.apps.account.managers import userManager

class userProfile(models.Model):
	GENDER = (
	('m', 'Male'),
	('f', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER, default='m')
	user = models.ForeignKey(User)