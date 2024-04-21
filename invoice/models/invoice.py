from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Invoice(models.Model):
    title = models.CharField(max_length=65)
    customer_name = models.CharField(max_length=255,null=True, blank=True)
    customer_contact =models.TextField(null=True, blank=True)
    description = models.TextField()
    total = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    is_approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='invoice', null=True, blank=True)

    
    def __str__(self):
        return self.title