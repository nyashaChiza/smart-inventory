from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Invoice(models.Model):
    title = models.CharField(max_length=65)
    customer_name = models.CharField(max_length=255,null=True, blank=True)
    customer_contact =models.TextField(null=True, blank=True)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='invoice', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)


    
    def __str__(self):
        return self.title
    
    def total_amount(self):
        return sum(item.sub_total() for item in self.invoice_items.all())