from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm, widgets
from ventas.models import Venta, DetalleVenta
class VentaForm(ModelForm):

    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["estado",]

   

class VentaUpdateForm(ModelForm):

    class Meta:
        model=Venta
        fields = "__all__"
        
class DetalleVentaForm(ModelForm):

    class Meta:
        model = DetalleVenta
        fields = "__all__"
        exclude=["estado",]


class DetalleVentaUpdateForm(ModelForm):

    class Meta:
        model=DetalleVenta
        fields = "__all__"
        