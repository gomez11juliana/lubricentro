from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm, widgets
from compras.models import Compra

class CompraForm(ModelForm):

    class Meta:
        model = Compra
        fields = "__all__"
        exclude=["estado",]

    

class CompraUpdateForm(ModelForm):

    class Meta:
        model=Compra
        fields = "__all__"
        
