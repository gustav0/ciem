from django.shortcuts import render_to_response
from ciem.apps.data.models import Entry

def index(request):
	entries = Entry.objects.published_entries().order_by('-id')
	ctx = { 'entries':entries }
	return render_to_response('homepage/index.html', ctx)

def about(request):
	return render_to_response('homepage/about.html')

def contact(request):
	return render_to_response('homepage/contact.html')

def register(request):
	return render_to_response('homepage/register.html')