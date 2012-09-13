from django.db import models
from django.contrib.auth.models import User
import datetime
from ciem.apps.account.managers import antropometricosManager
#from ciem.apps.account.managers import userManager

class userProfile(models.Model):
	GENERO = (('m', 'Masculino'),
	          ('f', 'Femenino'),
	          ('o', 'Otro'),
	         )
	genero = models.CharField(max_length=1, choices=GENERO, default='m')
	cedula = models.FloatField(default=1)
	fecha_nacimiento = models.DateField()
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
	fecha_creacion = models.DateField(auto_now_add=True)

	objects = antropometricosManager()