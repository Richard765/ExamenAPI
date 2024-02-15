from django.db import models

class Socio(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    numero_socio = models.IntegerField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dni} - {self.numero_socio}"
