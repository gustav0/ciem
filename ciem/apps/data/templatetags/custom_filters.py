from django.template import Library
from django.db.models import Count
from django.utils.safestring import mark_safe
from datetime import date


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
    #return mark_safe('<div class="noDisplayDiv"><select name="form-'+str(loop)+'-alimento" id="id_form-'+str(loop)+'-alimento"><option value="{{alimento.'+str(loop)+'.id}}">{{alimento.'+str(loop)+'.id}}</option></select><select name="form-'+str(loop)+'-frecuenciaConsumo" id="id_form-'+str(loop)+'-frecuenciaConsumo"><option value="{{perfilFrecuencia.0.id}}">{{perfilFrecuencia.0.id}}</option></select></div>')
