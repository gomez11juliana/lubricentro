from servicios.models import Servicio

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'