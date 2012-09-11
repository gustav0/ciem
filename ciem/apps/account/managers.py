from django.db import models

class antropometricosManager(models.Manager):
	def getAll(self):
		return self.model.objects.all()
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')