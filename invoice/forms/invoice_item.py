from django import forms
from invoice.models import InvoiceItem

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['invoice', 'product', 'quantity']
        widgets = {
            'invoice': forms.Select(attrs={'class': 'js-select2 form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
