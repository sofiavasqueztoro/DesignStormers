from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'producto',
            'color',
            'talla',
            'ubicacion'
        ]

        labels = {
            'variable' : 'Variable',
            'producto' : 'Producto',
            'color' : 'Color',
            'talla' : 'Talla',
            'ubicacion' : 'Ubicacion'
        }
