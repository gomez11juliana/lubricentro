from django.db import models
from productos.models import Producto

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField(auto_now_add=True)
    class Estado(models.TextChoices):
        ACTIVO='1',("Activo")
        INACTIVO='0',("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    def total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f'Compra de {self.cantidad} unidades de {self.producto}'


