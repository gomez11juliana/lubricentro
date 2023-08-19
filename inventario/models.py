from django.db import models

class Inventario(models.Model):
    nombre_repuesto=models.CharField(max_length=30,verbose_name="nombre del repuesto")
    tipo=models.CharField(max_length=20,verbose_name="tipo de repuesto")
    marca_respuesto=models.CharField(max_length=20, verbose_name="marca")

