from django import forms
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

#Crear Formulario
'''
class CreatePersona(forms.ModelForm):
    class Meta:
        model = models.Persona
        fields = ['email', 'rut', 'nom', 'tel', 'bday', 'region', 'ciudad', 'tviv']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()
'''
class PostForm(forms.ModelForm):
    
    class MetaPers:
        model = Persona       
        fields = ('rut', 'nombre', 'bday', 'email', 'tel', 'region', 'ciudad', 'tviv', )

    class MetaPerr:
        model = Perro   
        fields = ('Nombre', 'Raza', 'Descripcion', 'Fotografia', 'Estado', )