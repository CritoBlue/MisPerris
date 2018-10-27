from django import forms
from .models import Persona, Ciudad

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('email', 'rut', 'nom', 'tel', 'bday', 'region', 'ciudad', 'tviv')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()