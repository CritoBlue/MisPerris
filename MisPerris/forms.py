from django import forms
from . import models

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