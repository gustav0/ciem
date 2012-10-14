#!/usr/local/bin/python
# coding: latin-1
from django.shortcuts import render_to_response
from ciem.apps.data.forms import *
from ciem.apps.data.models import *


def pesoAlimento(request):
	form = pesoAlimentoForm(request.POST or None)
	if form.is_valid():
		form.save()
	alimentos = alimentos.objects.all()
	ctx= {'form':form,'alimentos':alimentos}
	return render_to_response('data/pesoAlimento.html', ctx, context_instance=RequestContext(request))
