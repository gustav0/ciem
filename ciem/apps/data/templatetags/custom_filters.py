# -*- encoding: utf-8 -*-
from django.template import Library
from django.db.models import Count
from django.utils.safestring import mark_safe
from datetime import date
from django.utils.encoding import force_unicode


register = Library()

@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
def get_index(value,list):
	mylista = value
	for i in range(list.count()):
		if list[i] == mylista:
			return int(i+1)
	return int(0)

def sumame_uno(value):
	return int(value)+1
@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
def get_int(value):
	return int(value)
@register.filter#OBTIENE RANGO PARA UN CICLO FOR
def get_range(value):
	return range(value)
@register.filter##OBTIENE RANGO PARA UN CICLO FOR DESDE 1
def get_range_from1(value):
	return range(1,value)
@register.filter#REGRESA LA LISTA EN EL INDEX INDICADO
def get_at_index(list, index):
	return list[index]
@register.filter#DIVIDIR UN STR
def split(str,splitter):
	return str.split(splitter)
@register.filter#PRIMERA LETRA MAYUS
def cap(value):
	namelist = value.split(' ')
	fixed = ''
	for name in namelist:
		name = name.lower()
		# fixes mcdunnough
		if name.startswith('mc'):
			sub = name.split('mc')
			name = "Mc" + sub[1].capitalize()
		# fixes "o'neill"
		elif name.startswith('o\''): 
			sub = name.split('o\'')
			name = "O'" + sub[1].capitalize()

		else: name = name.capitalize()
		
		nlist = name.split('-')
		for n in nlist:
			if len(n) > 1:
				up = n[0].upper()
				old = "-%s" % (n[0],)
				new = "-%s" % (up,)
				name = name.replace(old,new)

		fixed = fixed + " " + name
	return fixed
@register.filter#DEVUELVE EL PROGRESO ACTUAL DE LA FRECUENCIA DE CONSUMO
def count_by_len(var):
	count = len(list(var))
	return count

@register.filter#calcular edad
def calculate_age(born):
	today = date.today()
	try: # raised when birth date is February 29 and the current year is not a leap year
		birthday = born.replace(year=today.year)
	except ValueError:
		birthday = born.replace(year=today.year, day=born.day-1)
	if birthday > today:
		return today.year - born.year - 1
	else:
		return today.year - born.year

# AU= AUTH_USER, AU = ACCOUNT_USERPROFILE
# FILTROS ESPECIFICOS PARA AU
@register.filter#DEVUELVE FECHA DE NACIMIENTO
def au_getFechaNaciemiento(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].fecha_nacimiento
	return None

@register.filter#DEVUELVE EL APELLIDO
def au_getNombre(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].first_name
	return None

@register.filter#DEVUELVE EL PAIS
def au_getPais(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].pais
	return None

@register.filter#DEVUELVE EL NOMBRE
def au_getApellido(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].last_name
	return None

@register.filter#DEVUELVE GENERO DISPLAY
def au_getGenero(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].genero
	return None
@register.filter    
def au_getCedula(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].cedula
	return None

#|||||||||||||||||||||||||||||||||||||||#
#|FILTROS PARA LA FRECUENCIA DE CONSUMO|#
#|||||||||||||||||||||||||||||||||||||||#
@register.filter#DEVUELVE HTML PARA EL SELECT DEL ALIMENTO EN CADA FORM
def get_select_alimento(loop,list):
	return mark_safe('<select name="form-'+str(loop)+'-alimento" id="id_form-'+str(loop)+'-alimento"><option value="'+str(list[loop].id)+'"></option></select>')

@register.filter#DEVUELVE HTML PARA EL SELECT DEl PERFIL DEL USUARIO EN CADA FORM
def get_select_frecuencia(loop,list):
	return mark_safe('<select name="form-'+str(loop)+'-frecuenciaConsumo" id="id_form-'+str(loop)+'-frecuenciaConsumo"><option value="'+str(list[0].id)+'"></option></select>')

@register.filter#DEVUELVE DESCRIPCION DEL ALIMENTO PARA CADA PREGUNTA
def get_descripcion(loop,list):
	return list[loop].descripcion

@register.filter#DEVUELVE LA MEDIA DEL ALIMENTO PARA CADA PREGUNTA
def get_media(loop,list):
	return list[loop].media       

@register.filter#DEVUELVE LA MEDIA DEL ALIMENTO PARA CADA PREGUNTA
def get_radio_porcion(loop):
	return  mark_safe('<ul><li><input type="radio" id="id_form-'+str(loop)+'-porcion_p" value="p" name="form-'+str(loop)+'-porcion"></label></li><li><input type="radio" id="id_form-'+str(loop)+'-porcion_m" value="m" name="form-'+str(loop)+'-porcion" CHECKED ></li><li><input type="radio" id="id_form-'+str(loop)+'-porcion_g" value="g" name="form-'+str(loop)+'-porcion"></li></ul>')

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
#|FILTROS PARA LA FRECUENCIA DE CONSUMO                  |#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

@register.filter#DEVUELVE EL STRING DE LA FRECUENCIA
def parse_frecuencia(frecuencia):
	if int(frecuencia) == 0:    resultado = 'Nunca'
	elif int(frecuencia) == 1:  resultado = '1 vez al mes'
	elif int(frecuencia) == 2:  resultado = '2 - 3 al mes'
	elif int(frecuencia) == 3:  resultado = '1 por semana'
	elif int(frecuencia) == 4:  resultado = '2 por semana'
	elif int(frecuencia) == 5:  resultado = '3 - 4 por semana'
	elif int(frecuencia) == 6:  resultado = '5 - 6 por semana'
	elif int(frecuencia) == 6:  resultado = '1 vez por dia'
	elif int(frecuencia) == 6:  resultado = '2 o mas por dia'
	else:   resultado = 'error'
	return resultado

@register.filter#DEVUELVE EL STRING DE LA FRECUENCIA
def parse_porcion(porcion):
	if porcion =='p':   resultado = 'Pequeña'
	elif porcion =='m': resultado = 'Mediana'
	elif porcion =='g': resultado = 'Grande'
	else:   resultado = 'Grande'
	return resultado


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
#|FILTROS PARA LA FRECUENCIA DE CONSUMO DE NUTRICIONISTAS|#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
@register.filter#DEVUELVE EL PROGRESO ACTUAL DE LA FRECUENCIA DE CONSUMO
def get_progreso(var):
	progreso = 0
	for i in range(len(list(var))):
		if progreso < var[i].seccionnombre_id:
			progreso = var[i].seccionnombre_id
	return progreso


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
#|FILTROS PARA SABER SI UN USUARIO PERTENECE A UN GRUPO  |#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
@register.filter
def in_group(user, groups):
	"""Returns a boolean if the user is in the given group, or comma-separated
    list of groups.

    Usage::

        {% if user|in_group:"Friends" %}
        ...
        {% endif %}

    or::

        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}

    """
	if user.is_authenticated():
		group_list = force_unicode(groups).split(',')
		return bool(user.groups.filter(name__in=group_list).values('name'))
	else:
		return False