from django.db import models

class antropometricosManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')
		
class ipaqManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')