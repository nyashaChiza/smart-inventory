from django import forms
from invoice.models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['title', 'customer_name', 'customer_contact', 'description']
