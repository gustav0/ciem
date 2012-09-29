from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger
from ciem.apps.account.models import datosAntropometricos,userProfile,ipaq
from django.contrib.auth.models import User

@login_required(login_url='/login')
def perfilUsuarios(request):
	if request.user.has_perm('data.add_alimento') and request.user.has_perm('data.change_alimento'):
		getUser = request.GET.get('user',1)
		tipoPerfil = request.GET.get('p',0)
		nombre = None
		try:
			if getUser > 1:
				if not User.objects.filter(id=getUser):
					return HttpResponseRedirect("/perfiles/")
				if int(tipoPerfil)==1:
					perfil = datosAntropometricos.objects.getById(int(getUser))
				elif int(tipoPerfil)==2:
					perfil = ipaq.objects.getById(int(getUser))
				elif int(tipoPerfil)==3:
					perfil = datosAntropometricos.objects.getById(int(getUser))
				else:
					perfil = None
					tipoPerfil = 0
				nombre = User.objects.filter(id=getUser)
				usuario = userProfile.objects.filter(user=getUser)
			else:
				nombre = User.objects.all()
				usuario = userProfile.objects.all()
				perfil = None
		except ValueError:
			return HttpResponseRedirect("/perfiles/")
		ctx= {'nombre':nombre,'usuario':usuario,'perfil':perfil,'tipo':tipoPerfil, }	
		return render_to_response('nutricionista/perfilUsuarios.html', ctx, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/profile/")
	