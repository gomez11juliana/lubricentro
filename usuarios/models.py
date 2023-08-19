from django.db import models

class Usuario(models.Model):
    documento=models.IntegerField(max_length=15,verbose_name="Número Documento")
    nombre=models.CharField(max_length=35,verbose_name="Nombre")
    apellido=models.CharField(max_length=35,verbose_name="Apellido")

