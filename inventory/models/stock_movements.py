from django.db import models

class StockMovement(models.Model):
    MOVEMENT_TYPES = (('ADD','ADD'),('REMOVE','REMOVE'),('BREAKAGE','BREAKAGE'))
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    movement_quantity = models.IntegerField(default = 0)
    previous_quantity = models.IntegerField(default = 0)
    current_quantity = models.IntegerField(default = 0)
    movement_type = models.CharField(choices=MOVEMENT_TYPES ,  max_length=255)
    price = models.IntegerField(default = 0)
    stock = models.ForeignKey('inventory.Stock', on_delete=models.CASCADE , related_name='stock')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name