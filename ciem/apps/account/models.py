from django.db import models
from django.contrib.auth.models import User
import datetime
#from ciem.apps.account.managers import userManager

class userProfile(models.Model):
	GENDER = (('m', 'Male'),
	          ('f', 'Female'),
	         )
	gender = models.CharField(max_length=1, choices=GENDER, default='m')
	cedula = models.FloatField(default=1)
	fecha_nacimiento = models.DateField(default=datetime.date.today)
	user = models.ForeignKey(User)
