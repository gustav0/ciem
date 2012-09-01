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
	
class datosAntropometricos(models.Model):
	peso=models.DecimalField(max_digits=3, decimal_places=3, verbose_name='Peso')
	circunferencia_cintura= models.DecimalField(max_digits=3, decimal_places=3, verbose_name='Circunferencia de Cintura')
	circunferencia_cadera= models.DecimalField(max_digits=3, decimal_places=3, verbose_name='Circunferencia de Cadera')
	PATOLOGIA1=(
	 ('1','Si'),
	 ('0','No'),
	 )
	patologia1 = models.CharField(max_length=1, choices=PATOLOGIA1, default='0', verbose_name='Sufre usted de patologia1')
	user = models.ForeignKey(User)
	 