from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class JobCardItem(models.Model):
    stock = models.ForeignKey('inventory.Stock', on_delete=models.SET_NULL, related_name='job_card', null=True, blank=True)
    job_card = models.ForeignKey('job_card.JobCard', on_delete=models.SET_NULL, related_name='job_card_item', null=True, blank=True)
    quantity = models.IntegerField(default = 1)
    
    def total_cost(self):
        try:
            cost = self.quantity * self.part.price
        except Exception as e:
            cost = 0
        return cost 