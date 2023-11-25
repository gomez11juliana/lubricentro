from django.core.files.uploadedfile import UploadedFile
from django.forms import ModelForm, widgets
from usuarios.models import Usuario
class UsuarioForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["estado",]
        
        
    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento')
        telefono= cleaned_data.get('telefono')
        
    

        if documento and len(str(documento)) > 12:
            self.add_error('documento', "El documento no puede tener más de 12 dígitos")

        if telefono and len(str(telefono)) > 10:
            self.add_error('telefono_contacto', "El teléfono no puede tener más de 10 dígitos")

    
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        

class UsuarioUpdateForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["documento","rh"]
        
