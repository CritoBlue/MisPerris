from django.contrib import admin
from .models import Region, Ciudad, TipoVivienda, Raza, EstadoPerro, Persona, Perro

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(TipoVivienda)
admin.site.register(Raza)
admin.site.register(EstadoPerro)
admin.site.register(Persona)
admin.site.register(Perro)