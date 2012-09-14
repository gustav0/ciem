from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ciem.apps.account.models import datosAntropometricos,userProfile

@login_required(login_url='/login')
def perfilUsuarios(request):
	get_user = request.GET.get('user',1)
	if get_user!=0:
		usuario = userProfile.objects.filter(user_id=get_user)
	else:
		usuario = userProfile.objects.all()
	perfil = datosAntropometricos.objects.all()
	ctx= {'usuario':usuario, 'perfil':perfil,}	
	return render_to_response('nutricionista/perfilUsuarios.html', ctx, context_instance=RequestContext(request))
	