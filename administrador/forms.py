from django.forms import ModelForm, DateTimeInput, TimeInput
from .models import *

class RegistroForm(ModelForm):
    class Meta:
        model=Registro
        fields=['id_carta','pedido','folio','origen','destino','maniobras','diesel','gastos','hora_reporte','inicio_carga','termino_carga','inicio_ruta','arribo_cliente','inicio_descarga','termino_descarga','termino_viaje']
        widgets = {
            'hora_reporte': TimeInput(),
            'inicio_carga': DateTimeInput(),
            'termino_carga': DateTimeInput(),
            'inicio_ruta': DateTimeInput(),
            'arribo_cliente': DateTimeInput(),
            'inicio_descarga': DateTimeInput(),
            'termino_descarga': DateTimeInput(),
            'termino_viaje': DateTimeInput(),
        }