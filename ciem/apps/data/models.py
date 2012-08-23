from django.db import models
from ciem.apps.data.managers import EntryManager
from ciem.apps.data.managers import alimentoManager

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title   = models.CharField(max_length=64)
    text    = models.TextField()
    published = models.BooleanField(db_index=True, default=True)

    objects = EntryManager()

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.created) 

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