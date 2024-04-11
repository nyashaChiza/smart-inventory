from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    category = models.ForeignKey('inventory.Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name