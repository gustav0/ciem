from django.forms import ModelForm
from ciem.apps.articles.models import *
from django import forms
from datetime import datetime

class articleNuevoForm(ModelForm):
	
	"""
	DRAFT = 'draft'
	PUBLISHED = 'published'
	category = forms.ModelChoiceField(label="Categoria",queryset=Category.objects.all())
	title = forms.CharField(label='Titulo')
	body = forms.CharField(label='Cuerpo del articulo', widget=forms.Textarea())
	tags = forms.CharField(label='Etiquetas')
	publish_date = forms.DateTimeField(label='Fecha de publicacion', initial=datetime.now)
	status = forms.ChoiceField(label='Estatus del articulo',choices=((DRAFT, 'Draft'),(PUBLISHED, 'Published')))
	featured = forms.BooleanField(label='Destacados')
	slug = forms.CharField(label='Ficha')
	summary = forms.CharField(label='Resumen')
	snippet = forms.CharField(label='Fragmento', widget=forms.Textarea())
	"""
	class Meta:
		model = Article
		exclude = ['author','related_articles']