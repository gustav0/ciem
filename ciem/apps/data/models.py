from django.db import models
from ciem.apps.data.managers import EntryManager
from ciem.apps.data.managers import alimentoManager


class Entry(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    titulo   = models.CharField(max_length=64)
    texto    = models.TextField()
    publicado = models.BooleanField(db_index=True, default=True)

    objects = EntryManager()
    def __unicode__(self):
        return u"%s - %s" % (self.titulo, self.fecha_creacion) 


class alimento(models.Model):
	nombre = models.CharField(max_length=70)
	calorias = models.FloatField()
	humedad = models.FloatField()
	proteina = models.FloatField()
	grasas = models.FloatField()
	carbohidratos_disponibles = models.FloatField()
	carbohidratos_totales = models.FloatField()
	fibra_dietetica_total = models.FloatField()
	fibra_dietetica_insoluble = models.FloatField()
	cenizas = models.FloatField()
	calcio = models.FloatField()
	fosforo = models.FloatField()
	hierro = models.FloatField()
	magnesio = models.FloatField()
	zinc = models.FloatField()
	cobre = models.FloatField()
	sodio = models.FloatField()
	potasio = models.FloatField()
	vitamina_a = models.FloatField()
	caroteno_equivalente_total = models.FloatField()
	tiamina = models.FloatField()
	riboflavina = models.FloatField()
	niacina = models.FloatField()
	vitamina_b6 = models.FloatField()
	acido_ascorbico = models.FloatField()

	objects = alimentoManager()

	def __unicode__(self):
		return u"%s - %s" % (self.nombre, self.calorias) 

class pesoAlimento(models.Model):
	alimento = models.ForeignKey(alimento)
	MEDIDA =(('taza','taza'),('Cucharada','Cucharada'),('Cucharadita','Cucharadita'),('Unidad','Unidad'),('Rebanada','Rebanada'),('Casco','Casco'),('Porcion','Porcion'),('Onza','Onza'),('Trozo','Trozo'),('Chuleta','Chuleta'),('Bisteck','Bisteck'),('Rueda','Rueda'),('Filete','Filete'),('Lonja','Lonja') ) 
	numMedida= models.CharField(max_length=5, default='0')
	medida = models.CharField(max_length=70, choices=MEDIDA, default='Taza')
	peso = models.FloatField(default=0)	

	def __unicode__(self):
		return u"%s" % (self.alimento) 