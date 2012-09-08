#!/usr/local/bin/python
# coding: latin-1
from django.shortcuts import render_to_response
from ciem.apps.data.models import *
from ciem.apps.homepage.forms import *
from django.template import RequestContext
from django.core.mail import send_mail
from ciem.apps.homepage.forms import historiaForm
def index(request):
	ctx = {}
	return render_to_response('homepage/index.html', ctx,  context_instance=RequestContext(request))

def about(request):
	mision = "El Centro de Investigaciones Endocrino-Metabólicas Dr. Félix Gómez de la Facultad de Medicina de la Universidad del Zulia, es una organización sin fines de lucro cuyos pilares están sustentados en las actividades Universitarias de Investigación, Extensión y Docencia. Orientada hacia la promoción y desarrollo de programas y proyectos de Investigación básica y aplicada y en consonancia con la formación integral de estudiantes y profesionales de la Facultad de Medicina, ofrecemos un servicio médico integral a los pacientes con enfermedades endocrino-metabólicas del Estado Zulia. \n Identificada con el desarrollo académico, profesional, económico y humano de nuestros empleados, fomentamos un clima de compromiso y sentido de pertenencia en nuestra institución, trabajando con responsabilidad, mística y vocación de servicio apoyados en un personal altamente capacitado en conjunción con el uso de tecnologías limpias con bajo impacto ambiental, brindamos una atención de alta calidad, humana, oportuna y de bajo costo, constituyendo así un centro de referencia en el área endocrinológica."
	vision = "El Centro de Investigaciones Endocrino-Metabólicas Dr. Félix Gómez de la Facultad de Medicina de la Universidad del Zulia, es un centro líder en investigación clínica, básica y epidemiológica, así como en el desarrollo y producción de fármacos, tanto a nivel nacional como internacional, mediante el fortalecimiento de líneas de investigación y formación de recursos humanos, constituyendo así el organismo de referencia por excelencia para el diagnóstico, tratamiento y prevención de enfermedades endocrino-metabólicas, siendo nuestro norte el brindar una atención de alta calidad a nuestros pacientes mediante la actualización constante de nuestros empleados y tecnologías."
	ctx = {'mision': mision, 'vision':vision }
	return render_to_response('homepage/about.html', ctx, context_instance=RequestContext(request))

def contact(request):
	success = False
	email = ""
	asunto = ""
	texto = ""
	if request.method == "POST":
		contact_form = contactForm(request.POST)
		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			asunto = contact_form.cleaned_data['asunto']
			texto = contact_form.cleaned_data['texto']
			send_mail(asunto,"Email contacto: %s \nAsunto: %s \nTexto: %s" % (email,asunto,texto), 'ciem.luz.mail@gmail.com',['ciem.luz.mail@gmail.com'])
	else:
		contact_form = contactForm()
	ctx = {'contact_form':contact_form, 'email':email, 'asunto':asunto, 'texto':texto, 'success':success}
	return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

def calculadora(request):
	alimentos = alimento.objects.all().order_by('nombre')
	ctx={ 'alimentos':alimentos }
	return render_to_response('homepage/calculadora.html', ctx, context_instance=RequestContext(request))
	


def historia(request):
	if request.method =='POST':
		formulario = historiaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
	else:
		formulario=historiaForm()
	ctx= {'formulario':formulario,}
	return render_to_response('homepage/historia.html', ctx, context_instance=RequestContext(request))
	

