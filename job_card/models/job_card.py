from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobCard(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='job_card', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def total_amount(self):
        return sum(item.sub_total() for item in self.job_card_items.all())
    
    