from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

def index(request):
	return render(request, 'misperris/index.html')

def contacto(request):
	regions = Region.objects.all()
	cities = Ciudad.objects.all()
	tipoViv = TipoVivienda.objects.all()
	return render(request, 'misperris/contacto.html', {"regions" : regions, "cities" : cities, "types" : tipoViv})


def servicios(request):
	estado = EstadoPerro.objects.all()
	raza = Raza.objects.all()
	persona = Persona.objects.all()
	return render(request, 'misperris/servicios.html', {"estado" : estado, "raza" : raza, "persona" : persona})

'''
def create_persona (request):
	form = forms.CreatePersona()
	return render (request, 'misperris/contacto.html', {'form' : form})
'''