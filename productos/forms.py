from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm, widgets
from productos.models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["estado",]

    def clean(self):
        cleaned_data = super().clean()
        precio = cleaned_data.get('precio')
        
        if precio and len(str(precio))>200:
            self.add_error('precio',"El precio es invalido")
           
            return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductoForm,self).__init__(*args, **kwargs)

class ProductoUpdateForm(ModelForm):

    class Meta:
        model=Producto
        fields = "__all__"
        
