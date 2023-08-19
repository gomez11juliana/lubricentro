from django.db import models

class Servicio(models.Model):
    nombre_servicio=models.CharField(max_length=30,verbose_name="Nombre del servicio")
