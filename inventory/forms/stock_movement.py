from django import forms
from django.forms import ModelForm
from inventory.models import StockMovement
from django.forms import ModelForm, TextInput, Select


class StockMovementForm(ModelForm):
    class Meta:
        model = StockMovement
        fields = ('stock', 'movement_quantity','description', 'movement_type')
        
        widgets = {
            'stock': TextInput(attrs={'class': 'form-control'}),
            'movement_quantity': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'movement_type': Select(attrs={'class': 'form-control js-select2'}),
        }
        
        def is_valid(self, *args, **kwargs):
            return True
        
        