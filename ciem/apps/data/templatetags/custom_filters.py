from django.template import Library
from django.db.models import Count
from datetime import date


register = Library()

@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
def get_index(value,list):
	mylista = value
	for i in range(list.count()):
		if list[i] == mylista:
			return int(i+1)
	return int(0)
@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
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
@register.filter#DEVUELVE GENERO DISPLAY
def au_getGenero(list,mid):
	for i in range(list.count()):
		if list[i].id == mid:
			return list[i].genero
	return None