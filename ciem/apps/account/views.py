from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ciem.apps.account.forms import antropometricosForm, registerForm

def register(request):
	form = registerForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		user.backend = settings.AUTHENTICATION_BACKENDS[0]
		login(request, user)
		return redirect(reverse('account_profile'))
	ctx={'form': form,}
	return render_to_response('account/register.html', ctx, context_instance=RequestContext(request))
	
@login_required(login_url='/login')
def profile(request):
	ctx={'profile':request.user.get_profile(),}
	return render_to_response('account/profile.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def antropometricos(request):
	form = antropometricosForm(request.POST or None)
	form.user = 1;
	if form.is_valid():
		form.save()
	ctx= {'form':form, 'profile':request.user.get_profile(),}
	return render_to_response('account/datosAntropometricosForm.html', ctx, context_instance=RequestContext(request))	