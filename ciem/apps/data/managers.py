from django.db import models

class EntryManager(models.Manager):
	def published_entries(self):
		return self.model.objects.filter(published=True)

class alimentoManager(models.Manager):
	def getAll(self):
		return self.model.objects.all()
	def getByName(self,name):
		return self.model.objects.filter(nombre=str(name))
	def getById(self,id):
		return self.model.objects.filter(id=id)