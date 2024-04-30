from django import forms
from django.forms import ModelForm
from inventory.models import StockMovement
from django.forms import ModelForm, TextInput, Select, NumberInput


class StockMovementForm(ModelForm):
    class Meta:
        model = StockMovement
        fields = ('stock', 'movement_quantity','description', 'movement_type')
        
        widgets = {
            'stock': TextInput(attrs={'class': 'form-control'}),
            'movement_quantity': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'movement_type': Select(attrs={'class': 'form-control js-select2'}),
        }
        
        def is_valid(self, *args, **kwargs):
            return True
        
        