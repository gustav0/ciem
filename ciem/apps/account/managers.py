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