from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'color',
            'talla',
            'ubicacion',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'producto' : 'Producto',
            'color' : 'Color',
            'talla' : 'Talla',
            'ubicacion' : 'Ubicacion',
            #'dateTime' : 'Date Time',
        }
