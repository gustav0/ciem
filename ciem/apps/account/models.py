from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import datetime
from ciem.apps.account.managers import *
from ciem.apps.data.models import alimento
from ciem.apps.account.gestorDocumento import ContentTypeRestrictedFileField

#from ciem.apps.account.managers import userManager

class userProfile(models.Model):
	GENERO= (('m','Masculino'),('f','Femenino'),('o','Otro'),)
	PREGUNTA = ((1,'Segundo nombre de la abuela por parte de madre'),(2,'Apellido de maestro favorito de primaria'),(3,'Nombre de la primera mascota'),(4,'Primo(a) favorito'), (5, 'Personaje historico favorito'), (6, 'Ocupacion del abuelo'))
	genero = models.CharField(max_length=1, choices=GENERO, default='m')
	cedula = models.FloatField(default=1)
	fecha_nacimiento = models.DateField()
	pais = models.CharField(max_length=80)
	municipio = models.CharField(max_length=45)
	preguntaSecreta = models.CharField(max_length=1,choices=PREGUNTA,default = 1)
	respuestaSecreta = models.CharField(max_length=70)
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
	KG = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30),(31,31),(32,32),(33,33),(34,34),(35,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(43,43),(44,44),(45,45),(46,46),(47,47),(48,48),(49,49),(50,50),(51,51),(52,52),(53,53),(54,54),(55,55),(56,56),(57,57),(58,58),(59,59),(60,60),(61,61),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),(70,70),(71,71),(72,72),(73,73),(74,74),(75,75),(76,76),(77,77),(78,78),(79,79),(80,80),(81,81),(82,82),(83,83),(84,84),(85,85),(86,86),(87,87),(88,88),(89,89),(90,90),(91,91),(92,92),(93,93),(94,94),(95,95),(96,96),(97,97),(98,98),(99,99),(100,100),(101,101),(102,102),(103,103),(104,104),(105,105),(106,106),(107,107),(108,108),(109,109),(110,110),(111,111),(112,112),(113,113),(114,114),(115,115),(116,116),(117,117),(118,118),(119,119),(120,120),(121,121),(122,122),(123,123),(124,124),(125,125),(126,126),(127,127),(128,128),(129,129),(130,130),(131,131),(132,132),(133,133),(134,134),(135,135),(136,136),(137,137),(138,138),(139,139),(140,140),(141,141),(142,142),(143,143),(144,144),(145,145),(146,146),(147,147),(148,148),(149,149),(150,150),(151,151),(152,152),(153,153),(154,154),(155,155),(156,156),(157,157),(158,158),(159,159),(160,160),(161,161),(162,162),(163,163),(164,164),(165,165),(166,166),(167,167),(168,168),(169,169),(170,170),(171,171),(172,172),(173,173),(174,174),(175,175),(176,176),(177,177),(178,178),(179,179),(180,180),(181,181),(182,182),(183,183),(184,184),(185,185),(186,186),(187,187),(188,188),(189,189),(190,190),(191,191),(192,192),(193,193),(194,194),(195,195),(196,196),(197,197),(198,198),(199,199),(200,200),(201,201),(202,202),(203,203),(204,204),(205,205),(206,206),(207,207),(208,208),(209,209),(210,210),(211,211),(212,212),(213,213),(214,214),(215,215),(216,216),(217,217),(218,218),(219,219),(220,220),(221,221),(222,222),(223,223),(224,224),(225,225),(226,226),(227,227),(228,228),(229,229),(230,230),(231,231),(232,232),(233,233),(234,234),(235,235),(236,236),(237,237),(238,238),(239,239),(240,240),)
	CM = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30),(31,31),(32,32),(33,33),(34,34),(35,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(43,43),(44,44),(45,45),(46,46),(47,47),(48,48),(49,49),(50,50),(51,51),(52,52),(53,53),(54,54),(55,55),(56,56),(57,57),(58,58),(59,59),(60,60),(61,61),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),(70,70),(71,71),(72,72),(73,73),(74,74),(75,75),(76,76),(77,77),(78,78),(79,79),(80,80),(81,81),(82,82),(83,83),(84,84),(85,85),(86,86),(87,87),(88,88),(89,89),(90,90),(91,91),(92,92),(93,93),(94,94),(95,95),(96,96),(97,97),(98,98),(99,99),(100,100),(101,101),(102,102),(103,103),(104,104),(105,105),(106,106),(107,107),(108,108),(109,109),(110,110),(111,111),(112,112),(113,113),(114,114),(115,115),(116,116),(117,117),(118,118),(119,119),(120,120),(121,121),(122,122),(123,123),(124,124),(125,125),(126,126),(127,127),(128,128),(129,129),(130,130),(131,131),(132,132),(133,133),(134,134),(135,135),(136,136),(137,137),(138,138),(139,139),(140,140),(141,141),(142,142),(143,143),(144,144),(145,145),(146,146),(147,147),(148,148),(149,149),(150,150),(151,151),(152,152),(153,153),(154,154),(155,155),(156,156),(157,157),(158,158),(159,159),(160,160),(161,161),(162,162),(163,163),(164,164),(165,165),(166,166),(167,167),(168,168),(169,169),(170,170),(171,171),(172,172),(173,173),(174,174),(175,175),(176,176),(177,177),(178,178),(179,179),(180,180),(181,181),(182,182),(183,183),(184,184),(185,185),(186,186),(187,187),(188,188),(189,189),(190,190),(191,191),(192,192),(193,193),(194,194),(195,195),(196,196),(197,197),(198,198),(199,199),(200,200),(201,201),(202,202),(203,203),(204,204),(205,205),(206,206),(207,207),(208,208),(209,209),(210,210),(211,211),(212,212),(213,213),(214,214),(215,215),(216,216),(217,217),(218,218),(219,219),(220,220),(221,221),(222,222),(223,223),(224,224),(225,225),(226,226),(227,227),(228,228),(229,229),(230,230),(231,231),(232,232),(233,233),(234,234),(235,235),(236,236),(237,237),(238,238),(239,239),(240,240),) 
	peso=models.FloatField(default=0, choices=KG)
	circunferencia_cintura= models.FloatField(default=0,choices=CM)
	circunferencia_cadera= models.FloatField(default=0,choices=CM)
	estatura = models.FloatField(default=0,choices=CM)
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
	apreciacion_adiposidad = models.CharField(max_length=40) 
	obesidad = models.FloatField(default = 0)
	apreciacion_obesidad = models.CharField(max_length=40) 
	objects = antropometricosResultadoManager()
	apreciacion_cintura = models.CharField(max_length=80) 

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
	"""Datos para almacenar del recordatorio de 24 horas"""
	user = models.ForeignKey(User)
	fecha_creacion = models.DateField(auto_now_add=True)
	horaDesayuno = models.TimeField(max_length=40)
	desayuno = models.BooleanField(default=True)
	diasDesayuno =  models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	horaMerienda1 = models.TimeField(max_length=40)
	merienda1 = models.BooleanField(default=True)
	diasMerienda1 =  models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	horaAlmuerzo = models.TimeField(max_length=40)
	almuerzo = models.BooleanField(default=True)
	diasAlmuerzo =  models.IntegerField(default=7,validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	horaMerienda2 = models.TimeField(max_length=40)
	merienda2 = models.BooleanField(default=True)
	diasMerienda2 =  models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	horaCena = models.TimeField(max_length=40)
	cena = models.BooleanField(default=True)
	diasCena =  models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	horaMerienda3 = models.TimeField(max_length=40) 
	merienda3 = models.BooleanField(default=True)
	diasMerienda3 =  models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(7)])
	objects = recordatorioManager()


class alimentoRecordatorio(models.Model):
	datosRecordatorio = models.ForeignKey(datosRecordatorio)
	namealimento = models.CharField(max_length=40)
	tam = models.CharField(max_length=1)
	#alimento = models.ForeignKey(alimento)
	
class datosRecordatorioResultado(models.Model):
	recordatorio = models.ForeignKey(datosRecordatorio)

class preguntaSecreta(models.Model):
	pregunta = models.CharField(max_length=100)

