from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

def index(request):
	return render(request, 'misperris/index.html')

def contacto(request):
	regions = Region.objects.all()
	cities = Ciudad.objects.all()
	tipoViv = TipoVivienda.objects.all()
	return render(request, 'misperris/contacto.html', {"regions" : regions, "cities" : cities, "types" : tipoViv})

def servicios(request):
	return render(request, 'misperris/servicios.html')

'''
def create_persona (request):
	form = forms.CreatePersona()
	return render (request, 'misperris/contacto.html', {'form' : form})
'''