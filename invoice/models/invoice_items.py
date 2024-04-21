from django.db import models

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('invoice.Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey('inventory.Stock', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def sub_total(self):
        return self.quantity * self.unit_price