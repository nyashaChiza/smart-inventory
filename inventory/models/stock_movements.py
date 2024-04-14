from django.db import models

class StockMovement(models.Model):
    MOVEMENT_TYPES = (('ADD','ADD'),('SALE','SALE'),('BREAKAGE','BREAKAGE'))
    MOVEMENT_STATUSES = (('Pending','Pending'),('Approved','Approved'),('Flagged','Flagged'))
    
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    movement_quantity = models.IntegerField(default = 0)
    previous_quantity = models.IntegerField(default = 0)
    current_quantity = models.IntegerField(default = 0)
    movement_type = models.CharField(choices=MOVEMENT_TYPES , max_length=255)
    movement_status = models.CharField(choices=MOVEMENT_STATUSES , default='Pending', max_length=255)
    status_comment = models.TextField(blank=True, null=True) 
    price = models.IntegerField(default = 0)
    stock = models.ForeignKey('inventory.Stock', on_delete=models.CASCADE , related_name='movements')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.stock.name
    
    def total_cost(self) -> float:
        return self.price * self.movement_quantity