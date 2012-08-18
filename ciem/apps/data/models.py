from django.db import models
from ciem.apps.data.managers import EntryManager

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title   = models.CharField(max_length=64)
    text    = models.TextField()
    published = models.BooleanField(db_index=True, default=True)

    objects = EntryManager()

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.created) 

class Alimento(models.Model):
	nombre = models.CharField(max_length=70)
	calorias = models.FloatField()

	"""
   `calorias` float DEFAULT NULL,
  `humedad` float DEFAULT NULL,
  `proteina` float DEFAULT NULL,
  `grasas` float DEFAULT NULL,
  `carbohidratos_disponibles` float DEFAULT NULL,
  `carbohidratos_totales` float DEFAULT NULL,
  `fibra_dietetica_total` float DEFAULT NULL,
  `fibra_dietetica_insoluble` float DEFAULT NULL,
  `cenizas` float DEFAULT NULL,
  `calcio` float DEFAULT NULL,
  `fosforo` float DEFAULT NULL,
  `hierro` float DEFAULT NULL,
  `magnesio` float DEFAULT NULL,
  `zinc` float DEFAULT NULL,
  `cobre` float DEFAULT NULL,
  `sodio` float DEFAULT NULL,
  `potasio` float DEFAULT NULL,
  `vitamina_a` float DEFAULT NULL,
  `caroteno_equivalente_total` float DEFAULT NULL,
  `tiamina` float DEFAULT NULL,
  `riboflavina` float DEFAULT NULL,
  `niacina` float DEFAULT NULL,
  `vitamina_b6` float DEFAULT NULL,
  `acido_ascorbico` float DEFAULT NULL,"""

