from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .forms import RawFormPersona, RawFormPerro
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

def index(request):
	return render(request, 'misperris/index.html')

def base_layout(request):
	return render(request, 'misperris/base_page.html')

def quienes_somos(request):
	return render(request, 'misperris/quienes_somos.html')

def login(request):
	return render(request, 'misperris/login.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'misperris/index.html')

def servicios(request):
	estado = EstadoPerro.objects.all()
	raza = Raza.objects.all()
	persona = Persona.objects.all()
	dogform = RawFormPerro()

	if request.method == 'POST':
		dogform = RawFormPerro(request.POST)
		if dogform.is_valid():
			Perro.objects.create(**dogform.cleaned_data)
			dogform = RawFormPerro()
		else:
			print(dogform.errors)

	context = {
		"form": dogform,
		"estado" : estado,
		"raza" : raza,
		"persona" : persona
	}
	return render(request, 'misperris/servicios.html', context)

def contacto(request):
	regions = Region.objects.all()
	cities = Ciudad.objects.all()
	tipoViv = TipoVivienda.objects.all()
	myform = RawFormPersona()

	if request.method == 'POST':
		myform = RawFormPersona(request.POST)
		if myform.is_valid():
			Persona.objects.create(**myform.cleaned_data)
			myform = RawFormPersona()
		else:
			print(myform.errors)

	context = {
		"form" : myform,
		"regions" : regions,
		"cities" : cities,
		"types" : tipoViv
	}
	return render(request, 'misperris/contacto.html', context)
