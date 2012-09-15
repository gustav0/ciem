from django.template import Library
from django.db.models import Count

register = Library()

@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
def get_index(value,list):
	mylista = value
	for i in range(list.count()):
		if list[i] == mylista:
			return i+1
	return 0

@register.filter#DEVUELVE LISTA DEL 0 AL NUMERO INDICADO
def sumame_uno(value):
	return int(value)+1

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
