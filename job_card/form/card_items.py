from django import forms
from job_card.models import JobCardItem

class JobCardItemForm(forms.ModelForm):
    class Meta:
        model = JobCardItem
        fields = ['job_card', 'stock', 'quantity']
        widgets = {
            'job_card': forms.Select(attrs={'class': 'js-select2 form-control'}),
            'stock': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
