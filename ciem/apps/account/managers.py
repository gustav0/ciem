from django.db import models
from django.contrib.auth.models import User

class antropometricosManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')
	def getByIdJoin(self,id):
		query='SELECT data.*,resultado.metabolismobasal,resultado.indiceAdiposidad,resultado.obesidad,resultado.apreciacion_obesidad,resultado.apreciacion_cintura,resultado.apreciacion_adiposidad FROM account_datosantropometricos as data INNER JOIN account_antropometricosresultado as resultado ON data.id=resultado.datosantropometricos_id where data.user_id='+str(id)+' order by -data.fecha_creacion;'
		return self.model.objects.raw(query)
	def getForPerfil(self,id):
		query='SELECT data.id,resultado.apreciacion_obesidad FROM account_datosantropometricos as data INNER JOIN account_antropometricosresultado as resultado ON data.id=resultado.datosantropometricos_id where data.user_id='+str(id)+' ORDER BY -fecha_creacion;'
		return self.model.objects.raw(query)

class userProfileManager(models.Manager):
	def getUserJoin(self,id):
		query='SELECT * FROM auth_user as u INNER JOIN account_userprofile as p ON u.id=p.user_id WHERE u.id='+str(id)+';'
		return self.model.objects.raw(query)
	def getAllUser(self):
		query2='SELECT * FROM auth_user as u INNER JOIN account_userprofile as p ON u.id=p.user_id;'
		return self.model.objects.raw(query2)				
			
class ipaqManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')

class ipaqResultadoManager(models.Manager):
	def getResultados(self,id):
		query='SELECT * FROM account_ipaq as u INNER JOIN account_ipaqresultado as p ON u.id=p.ipaq_id WHERE u.user_id='+str(id)++' order by -data.fecha_creacion;'
		return self.model.objects.raw(query)
	
class antropometricosResultadoManager(models.Manager):
	def getById(self,id):
		return self.model.objects.raw(datosAntropometricos_id=id).order_by('-datosAntropometricos')

class frecuenciaConsumoManager(models.Manager):
	def getById(self,id):
		return self.model.objects.filter(user_id=id).order_by('-fecha_creacion')
	def getDataById(self,id):
		query='SELECT c.id,a.progreso,b.porcion,b.frecuencia,c.seccionnombre_id,c.descripcion,c.media FROM (account_frecuenciaconsumo as a left join account_datafrecuenciaconsumo as b on a.id=b.frecuenciaconsumo_id) left join account_alimentofrecuencia as c on b.alimento_id=c.id  where a.user_id='+str(id)+';'
		return self.model.objects.raw(query)

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

class recordatorioManager(models.Manager):
	"""Manejador del recordatorio de 24 horas"""
	def getById(self,id):
		return	self.model.objects.filter(user_id=id).order_by('-fecha_creacion')


