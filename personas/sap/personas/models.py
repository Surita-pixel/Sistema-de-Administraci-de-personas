from django.db import models

# Create your models here.
class Domicilio(models.Model):
    ciudad = models.CharField(max_length=225)
    barrio = models.CharField(max_length=225)
    no_avenida = models.IntegerField()
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=225)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=225)
    apellido = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'


