from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def profile(request):
	ctx={'profile':request.user.get_profile(),}
	return render_to_response('account/profile.html', ctx, context_instance=RequestContext(request))