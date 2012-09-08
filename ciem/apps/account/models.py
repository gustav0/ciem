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

	
class datosAntropometricos(models.Model):
	peso=models.FloatField(default=0, verbose_name='Peso')
	circunferencia_cintura= models.FloatField(default=0, verbose_name='Circunferencia de Cintura')
	circunferencia_cadera= models.FloatField(default=0, verbose_name='Circunferencia de Cadera')
	talla= models.FloatField(default=0, verbose_name='Talla')
	patologia1 = models.BooleanField(verbose_name="Patologia 1")
	patologia2 = models.BooleanField(verbose_name="Patologia 2")
	patologia3 = models.BooleanField(verbose_name="Patologia 3")
	user = models.ForeignKey(User)
	

