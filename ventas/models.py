from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario
from productos.models import Producto
# Create your models here.

class Venta(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto= models.ManyToManyField(Producto, through='DetalleVenta')
    fechaVenta=models.DateField(max_length=12, verbose_name="Fecha Venta")
    totalVenta=models.DecimalField(max_digits=10, decimal_places=2)
    class Estado(models.TextChoices):
        ACTIVO='1',("Activo")
        INACTIVO='0',("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    
    def __str__(self):
        return f'Venta de {self.usuarios} el {self.fechaVenta}'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de {self.producto} en {self.venta}'
