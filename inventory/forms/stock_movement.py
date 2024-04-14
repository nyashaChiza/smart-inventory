from django import forms
from django.forms import ModelForm

from inventory.models import StockMovement


class StockMovementForm(ModelForm):
    class Meta:
        model = StockMovement
        fields = ('stock', 'movement_quantity','description', 'movement_type')
        
        def is_valid(self, *args, **kwargs):
            return True
        
        