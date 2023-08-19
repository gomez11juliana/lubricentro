from inventario.models import Inventario

class InventarioForm(forms.ModelForm):
    
    class Meta:
        model = Inventario
        fields = '__all__'