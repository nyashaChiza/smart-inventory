from django import forms
from django.forms import ModelForm
from inventory.models import StockMovement
from django.forms import ModelForm, TextInput, Select


class AssessmentForm(ModelForm):
    class Meta:
        model = StockMovement
        fields = ('movement_status', 'status_comment')
        
        widgets = {
            'status_comment': TextInput(attrs={'class': 'form-control'}),
            'movement_status': Select(attrs={'class': 'form-control js-select2'}),
        }
        
        def is_valid(self, *args, **kwargs):
            return True
        
        