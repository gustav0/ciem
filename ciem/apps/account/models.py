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

class ipaq(models.Model):
	dias = ( ('0','1'),('1','2'),('2','3'),('3','4'),('4','5'),('5','6'),('6','7'), )
	horas = ( ('0','-'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('10','7+'), )
	minutos = ( ('0','-'),('1','5'),('2','10'),('3','15'),('4','30'),('5','45'), )

	p2a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p2b_trabajo = models.BooleanField()
	p3a_trabajo = models.CharField(max_length=1, choices=horas, default='0')
	p3b_trabajo = models.CharField(max_length=1, choices=minutos, default='0')


	p4a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p4b_trabajo = models.BooleanField()
	p5a_trabajo = models.CharField(max_length=1, choices=horas, default='0')
	p5b_trabajo = models.CharField(max_length=1, choices=minutos, default='0')	

	p6a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p6b_trabajo = models.BooleanField()
	p7a_trabajo = models.CharField(max_length=1, choices=horas, default='0')
	p7b_trabajo = models.CharField(max_length=1, choices=minutos, default='0')
	
	p8a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p8b_transporte = models.BooleanField()
	p9a_transporte = models.CharField(max_length=1, choices=horas, default='0')
	p9b_transporte = models.CharField(max_length=1, choices=minutos, default='0')

	p10a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p10b_transporte =models.BooleanField()
	p11a_transporte = models.CharField(max_length=1, choices=horas, default='0')
	p11b_transporte = models.CharField(max_length=1, choices=minutos, default='0')
	
	p12a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p12b_transporte = models.BooleanField()
	p13a_transporte = models.CharField(max_length=1, choices=horas, default='0')
	p13b_transporte = models.CharField(max_length=1, choices=minutos, default='0')
	
	p14a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p14b_hogar =models.BooleanField()
	p15a_hogar = models.CharField(max_length=1, choices=horas, default='0')
	p15b_hogar = models.CharField(max_length=1, choices=minutos, default='0')
	
	p16a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p16b_hogar = models.BooleanField()
	p17a_hogar = models.CharField(max_length=1, choices=horas, default='0')
	p17b_hogar = models.CharField(max_length=1, choices=minutos, default='0')
	
	p18a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p18b_hogar = models.BooleanField()
	p19a_hogar = models.CharField(max_length=1, choices=horas, default='0')
	p19b_hogar = models.CharField(max_length=1, choices=minutos, default='0')
	
	p20a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p20b_recreacion = models.BooleanField()
	p21a_recreacion = models.CharField(max_length=1, choices=horas, default='0')
	p21b_recreacion = models.CharField(max_length=1, choices=minutos, default='0')
	
	p22a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p22b_recreacion = models.BooleanField()
	p23a_recreacion = models.CharField(max_length=1, choices=horas, default='0')
	p23b_recreacion = models.CharField(max_length=1, choices=minutos, default='0')
	
	p24a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p24b_recreacion = models.BooleanField()
	p25a_recreacion = models.CharField(max_length=1, choices=horas, default='0')
	p25b_recreacion = models.CharField(max_length=1, choices=minutos, default='0')
	
	p26a_sentado = models.CharField(max_length=1, choices=dias, default='0')
	p26b_sentado = models.BooleanField()
	p27a_sentado = models.CharField(max_length=1, choices=horas, default='0')
	p27b_sentado = models.CharField(max_length=1, choices=minutos, default='0')