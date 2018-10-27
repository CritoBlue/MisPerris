from django.db import models

class Region(models.Model):
	nombre = models.CharField(max_length=30)
def __str__(self):
    return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
		
class TipoVivienda(models.Model):
    desc = models.CharField(max_length=25)
    def __str__(self):
        return self.desc

class Raza(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class EstadoPerro(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    tviv = models.ForeignKey(TipoVivienda, on_delete=models.SET_NULL, null=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    tel = models.IntegerField()
    bday = models.DateTimeField('Fecha de Nacimiento')
    def __str__(self):
        return self.nombre

class Perro(models.Model):
    raza = models.ForeignKey(Raza, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(EstadoPerro, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre