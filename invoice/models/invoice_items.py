from django.db import models

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('invoice.Invoice', on_delete=models.CASCADE, related_name='invoice_items')
    product = models.ForeignKey('inventory.Stock', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    
    def __str__(self):
        return f"{self.product}"

    def sub_total(self):
        return self.quantity * self.unit_price
    
