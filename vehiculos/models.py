from django.db import models

class Vehiculo(models.Model):
    placa=models.CharField(max_length=6,verbose_name="Placa")
    marca=models.CharField(max_length=20,verbose_name="Marca")
