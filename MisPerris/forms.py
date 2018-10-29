from django import forms
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

class RawFormPersona(forms.Form):
    rut = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ej: 12345678-9"}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ej: Pedro Juan Pérez López"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ejemplo@ejemplo.com"}))
    tel = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={"placeholder": "ej: 912345678"}))
    bday = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={"placeholder": "ej: 01/01/2000", 'class':'datepicker'})
        )
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Seleccione...")
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), empty_label="Seleccione...")
    tviv = forms.ModelChoiceField(label='Tipo de Vivienda' ,queryset=TipoVivienda.objects.all(), empty_label="Seleccione...")

class RawFormPerro(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ej: Cholito"}))
    desc = forms.CharField(label='Descripción', widget=forms.TextInput(attrs={"placeholder": "ej: Le gusta jugar"}))
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label="Seleccione...")
    estado = forms.ModelChoiceField(queryset=EstadoPerro.objects.all(), empty_label="Seleccione...")
    persona = forms.ModelChoiceField(label='Antiguo Dueño', queryset=Persona.objects.all(), empty_label="Busque su nombre...")