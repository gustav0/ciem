from django.db import models

class antropometricosManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')
	def getByIdJoin(self,id):
		query='SELECT * FROM account_datosantropometricos as data INNER JOIN account_antropometricosresultado as resultado ON data.id=resultado.datosantropometricos_id where data.user_id='+str(id)+';'
		return self.model.objects.raw(query)

class ipaqManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')
	
class antropometricosResultadoManager(models.Manager):
	def getById(self,id):
		return self.model.objects.raw(datosAntropometricos_id=id).order_by('-datosAntropometricos')

class frecuenciaConsumoManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')

	def upgradeProgreso(self,id,progreso):
		query = self.model.objects.get(user_id=id)
		query.progreso = progreso
		query.save()
		return query

class dataFrecuenciaConsumoManager(models.Manager):
	def getByIdAndSeccion(self,id,seccion):
		return self.model.objects.filter(user_id=id).filter(seccion=id).order_by('-fecha_creacion')

class alimentoFrecuenciaManager(models.Manager):
	def getById(self,idSeccion):
		return self.model.objects.filter(seccionNombre=idSeccion)