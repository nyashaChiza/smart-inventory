from django.db import models


# Create your models here.
class JobCardItem(models.Model):
    stock = models.ForeignKey('inventory.Stock', on_delete=models.SET_NULL, related_name='job_card', null=True, blank=True)
    job_card = models.ForeignKey('job_card.JobCard', on_delete=models.SET_NULL, related_name='job_card_items', null=True, blank=True)
    quantity = models.IntegerField(default = 1)
    unit_price = models.IntegerField(default = 1)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def sub_total(self):
        return self.quantity * self.unit_price
    
    def __str__(self) -> str:
        return f"{self.stock}"
    