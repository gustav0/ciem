#!/usr/local/bin/python
# coding: latin-1
from django import forms
from ciem.apps.data.models import *

class pesoAlimentoForm(ModelForm):
	class Meta:
		model = pesoAlimento