from personas.models import Domicilio
from django.forms import ModelForm, NumberInput

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': NumberInput(),
            'no_avenida': NumberInput()
        }