from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
	return render(request, 'misperris/index.html')

def contacto(request):
	return render(request, 'misperris/contacto.html')

def servicios(request):
	return render(request, 'misperris/servicios.html')

'''
def create_persona (request):
	form = forms.CreatePersona()
	return render (request, 'misperris/contacto.html', {'form' : form})
'''