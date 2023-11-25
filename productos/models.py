from django.db import models
from django.utils.translation import gettext_lazy as _
class Producto(models.Model):
    nombreProducto=models.CharField(max_length=45,verbose_name="Nombre Producto")
    descripcion=models.CharField(max_length=45,verbose_name="Descripcion")
    class Categoria(models.TextChoices):
        ACCESORIOS='ACCESORIOS',("Accesorios")
        RESPUESTOS='RESPUESTOS',("Repuestos")
        CONSUMIBLES='CONSUMIBLES',("Consumibles")
    categoria=models.CharField(max_length=11,choices=Categoria.choices,verbose_name="Categoria")
    precio=models.IntegerField(verbose_name="precio")
    class Estado(models.TextChoices):
        ACTIVO='1',("Activo")
        INACTIVO='0',("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    
    def clean(self):
        self.nombreProducto=self.nombreProducto.title()
    
    def __str__(self):
        return "%s %s"%(self.nombreProducto)
    class Meta:
        verbose_name_plural = "Productos"
