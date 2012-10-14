from django.db import models
from django.contrib.auth.models import User
import datetime
from ciem.apps.account.managers import *
from ciem.apps.account.gestorDocumento import ContentTypeRestrictedFileField

#from ciem.apps.account.managers import userManager

class userProfile(models.Model):
	GENERO = (('m', 'Masculino'),
	          ('f', 'Femenino'),
	          ('o', 'Otro'),
	         )
	genero = models.CharField(max_length=1, choices=GENERO, default='m')
	cedula = models.FloatField(default=1)
	fecha_nacimiento = models.DateField()
	pais = models.CharField(max_length=45)
	municipio = models.CharField(max_length=45)
	user = models.ForeignKey(User)
	objects = userProfileManager()

class profesional(models.Model):
	user = models.ForeignKey(User)
	profesion =models.CharField(max_length=100)
	universidad = models.CharField(max_length=200)
	trabajo = models.CharField(max_length=200)
	comentario = models.TextField()
	telefono = models.CharField(max_length=30,help_text="ej:0261-7235420")
	curriculum = ContentTypeRestrictedFileField(upload_to='curriculums', content_types=['application/pdf','application/zip','application/msword','word/document.xml','text/plain','application/vnd.oasis.opendocument.text'], max_upload_size=5242880)

class datosAntropometricos(models.Model):
	peso=models.FloatField(default=0)
	circunferencia_cintura= models.FloatField(default=0)
	circunferencia_cadera= models.FloatField(default=0)
	estatura = models.FloatField(default=0)
	hipertencion = models.BooleanField()
	diabetes = models.BooleanField()
	cancer = models.BooleanField()
	colesterol = models.BooleanField()
	trigliceridos = models.BooleanField()
	user = models.ForeignKey(User)
	fecha_creacion = models.DateField(auto_now_add=True)

	objects = antropometricosManager()

class antropometricosResultado(models.Model):
	datosAntropometricos = models.ForeignKey(datosAntropometricos)
	metabolismoBasal = models.FloatField(default = 0)
	requerimientoCaloricoDiario = models.FloatField(default = 0)
	indiceAdiposidad = models.FloatField(default = 0)
	obesidad = models.FloatField(default = 0)
	objects = antropometricosResultadoManager()

class ipaq(models.Model):
	user = models.ForeignKey(User)
	dias = ( ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'), )
	horas = ( ('0','-'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('10','7+'), )
	minutos = ( ('0','-'),('10','10'),('15','15'),('20','20'),('30','30'),('40','40'),('45','45') )

	p2a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p2b_trabajo = models.BooleanField(default=False)
	p3a_trabajo = models.CharField(max_length=2, choices=horas, default='0')
	p3b_trabajo = models.CharField(max_length=2, choices=minutos, default='0')
	p4a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p4b_trabajo = models.BooleanField(default=False)
	p5a_trabajo = models.CharField(max_length=2, choices=horas, default='0')
	p5b_trabajo = models.CharField(max_length=2, choices=minutos, default='0')	
	p6a_trabajo = models.CharField(max_length=1, choices=dias, default='0')
	p6b_trabajo = models.BooleanField(default=False)
	p7a_trabajo = models.CharField(max_length=2, choices=horas, default='0')
	p7b_trabajo = models.CharField(max_length=2, choices=minutos, default='0')
	p8a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p8b_transporte = models.BooleanField(default=False)
	p9a_transporte = models.CharField(max_length=2, choices=horas, default='0')
	p9b_transporte = models.CharField(max_length=2, choices=minutos, default='0')
	p10a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p10b_transporte =models.BooleanField(default=False)
	p11a_transporte = models.CharField(max_length=2, choices=horas, default='0')
	p11b_transporte = models.CharField(max_length=2, choices=minutos, default='0')
	p12a_transporte = models.CharField(max_length=1, choices=dias, default='0')
	p12b_transporte = models.BooleanField(default=False)
	p13a_transporte = models.CharField(max_length=2, choices=horas, default='0')
	p13b_transporte = models.CharField(max_length=2, choices=minutos, default='0')
	p14a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p14b_hogar =models.BooleanField(default=False)
	p15a_hogar = models.CharField(max_length=2, choices=horas, default='0')
	p15b_hogar = models.CharField(max_length=2, choices=minutos, default='0')
	p16a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p16b_hogar = models.BooleanField(default=False)
	p17a_hogar = models.CharField(max_length=2, choices=horas, default='0')
	p17b_hogar = models.CharField(max_length=2, choices=minutos, default='0')
	p18a_hogar = models.CharField(max_length=1, choices=dias, default='0')
	p18b_hogar = models.BooleanField(default=False)
	p19a_hogar = models.CharField(max_length=2, choices=horas, default='0')
	p19b_hogar = models.CharField(max_length=2, choices=minutos, default='0')
	p20a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p20b_recreacion = models.BooleanField(default=False)
	p21a_recreacion = models.CharField(max_length=2, choices=horas, default='0')
	p21b_recreacion = models.CharField(max_length=2, choices=minutos, default='0')
	p22a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p22b_recreacion = models.BooleanField(default=False)
	p23a_recreacion = models.CharField(max_length=2, choices=horas, default='0')
	p23b_recreacion = models.CharField(max_length=2, choices=minutos, default='0')
	p24a_recreacion = models.CharField(max_length=1, choices=dias, default='0')
	p24b_recreacion = models.BooleanField(default=False)
	p25a_recreacion = models.CharField(max_length=2, choices=horas, default='0')
	p25b_recreacion = models.CharField(max_length=2, choices=minutos, default='0')
	p26a_sentado = models.CharField(max_length=2, choices=horas, default='0')
	p26b_sentado = models.CharField(max_length=2, choices=minutos, default='0')
	p27a_sentado = models.CharField(max_length=2, choices=horas, default='0')
	p27b_sentado = models.CharField(max_length=2, choices=minutos, default='0')
	objects = ipaqManager()

class ipaqResultado(models.Model):
	ipaq = models.ForeignKey(ipaq)
	metTrabajo = models.FloatField(default=0)
	metTransporte = models.FloatField(default=0)
	metHogar = models.FloatField(default=0)
	metRecreacion = models.FloatField(default=0)
	metRecreacion = models.FloatField(default=0)
	tiempoAndar = models.FloatField(default=0)
	tiempoModerado= models.FloatField(default=0)
	tiempoVigoroso= models.FloatField(default=0)
	metTotalAndar = models.FloatField(default=0)
	metAndarTrabajo = models.FloatField(default=0)
	metAndarTransporte = models.FloatField(default=0)
	metAndarRecreacion = models.FloatField(default=0)
	metVigorosoTrabajo = models.FloatField(default=0)
	metVigorosoRecreacion = models.FloatField(default=0)
	metVigorosoHogar = models.FloatField(default=0)
	metModeradoHogar = models.FloatField(default=0)
	metModeradoJHogar = models.FloatField(default=0)
	metModeradoTrabajo = models.FloatField(default=0)
	metModeradoTransporte = models.FloatField(default=0)
	metModeradoRecreacion = models.FloatField(default=0)
	metTotalModerado = models.FloatField(default=0)
	metTotalVigoroso = models.FloatField(default=0)
	diasTotalAndar = models.FloatField(default=0)
	diasTotalModerado = models.FloatField(default=0)
	diasTotalVigoroso = models.FloatField(default=0)
	diasTotal= models.FloatField(default=0)
	metTotal= models.FloatField(default=0)
	resultadoDiscreto = models.FloatField(default=0)
	tiempoSentado = models.FloatField(default=0)
	MediaSentado = models.FloatField(default=0)
	minVigorosoTrabajo = models.FloatField(default=0)
	minAndarTrabajo = models.FloatField(default=0)
	minModeradoTrabajo = models.FloatField(default=0)
	minModeradoTransporte = models.FloatField(default=0)
	minAndarTransporte = models.FloatField(default=0)
	minModeradoJHogar = models.FloatField(default=0)
	minVigorosoHogar = models.FloatField(default=0)
	minModeradoHogar = models.FloatField(default=0)
	minVigorosoRecre = models.FloatField(default=0)
	minModeradoRecre = models.FloatField(default=0)
	minAndarRecre = models.FloatField(default=0)
	trabaja = models.FloatField(default=0)
	minVehiculo= models.FloatField(default=0) 
	objects = ipaqResultadoManager()

class frecuenciaConsumo(models.Model):
	user = models.ForeignKey(User,unique=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	progreso = models.CharField(max_length=1,default='0')

	objects = frecuenciaConsumoManager()


class nombreSeccionFrecuenciaConsumo(models.Model):
	descripcion = models.CharField(max_length=100,)

class alimentoFrecuencia(models.Model):
	seccionNombre = models.ForeignKey(nombreSeccionFrecuenciaConsumo)
	descripcion = models.CharField(max_length=100,)
	media = models.CharField(max_length=40,)
	objects = alimentoFrecuenciaManager()
	
class dataFrecuenciaConsumo(models.Model):
	FRECUENCIA = (('0','Nunca'),('1','1 vez al mes'),('2','2 - 3 veces al mes'),('3','1 por semana'),('4','2 por semana'),('5','3 - 4 por semana'),('6','5 - 6 por semana'),('7','1 vez por dia'),('8','2 o mas por dia'))
	frecuenciaConsumo = models.ForeignKey(frecuenciaConsumo)
	alimento = models.ForeignKey(alimentoFrecuencia)
	porcion = models.CharField(max_length=1, default='m')
	frecuencia = models.CharField(max_length=1, choices=FRECUENCIA, default='0')

	objects = dataFrecuenciaConsumoManager()

class datosRecordatorio(models.Model):
	"""Datos para almacenar del recordatori de 24 horas"""
	SIONO = (('s','si'),('n','no'))
	horaDesayuno = models.CharField(max_length=40)

	horaMerienda1 = models.CharField(max_length=40)
	horaAlmuerzo = models.CharField(max_length=40)
	horaMerienda2 = models.CharField(max_length=40)
	horaCena = models.CharField(max_length=40)
	horaMerienda3 = models.CharField(max_length=40) 
	objects = recordatorioManager()
