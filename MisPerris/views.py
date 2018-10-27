from django.shortcuts import render

def index(request):
	return render(request, 'misperris/index.html')

def contacto(request):
	return render(request, 'misperris/contacto.html')

def servicios(request):
	return render(request, 'misperris/servicios.html')