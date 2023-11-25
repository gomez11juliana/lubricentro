from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombres",default="Nombres")
    apellido= models.CharField(max_length=45,verbose_name="Apellidos", default="Apellidos") 
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        NIT='NIT',_("NIT")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extranjería")
    tipo_documento=models.CharField(max_length=20,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    class RH(models.TextChoices):
        OP='OP',_("O+")
        ON='ON',_("O-")
        AP='AP',_("A+")
        AN='AN',_("A-")
        BP='BP',_("B+")
        BN='BN',_("B-")
        ABP='ABP',_("AB+")
        ABN='ABN',_("AB-")
        
    rh= models.CharField(max_length=3,choices=RH.choices,verbose_name="Factor RH")
    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR='A',_("Administrador")
        SECRETARIA='S',_("Secretaria")    
    tipoUsuario=models.CharField(max_length=2,choices=TipoUsuario.choices,verbose_name="tipoUsuario", default="Administrador")
    correo= models.EmailField(max_length=50, verbose_name="Correo",default="lubricentro@gmail.com")
    telefono=models.PositiveIntegerField(verbose_name="Teléfono",default="3149675543")
    direccion=models.CharField(max_length=15,verbose_name="Dirección", default="cra3 #4-5")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
   
        
    def clean(self):
        self.nombre= self.nombre.title() 
        self.apellido= self.apellido.title()
        self.correo= self.correo.lower()
        
                
    def __str__(self):
        return "%s %s"%(self.nombre,self.apellido)
    
    class Meta:
        verbose_name_plural = "Usuarios"


