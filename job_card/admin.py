from django.contrib import admin
from .models import JobCard, JobCardItem

# Register your models here.

@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_approved', 'user', 'created', 'updated', 'total_amount')
    list_filter = ('is_approved', 'created', 'updated')
    search_fields = ('title', 'description')
    readonly_fields = ('total_amount',)

@admin.register(JobCardItem)
class JobCardItemAdmin(admin.ModelAdmin):
    list_display = ('stock', 'job_card', 'quantity', 'unit_price', 'created', 'updated', 'sub_total')
    list_filter = ('created', 'updated')
    search_fields = ('stock__name', 'job_card__title')
    readonly_fields = ('sub_total',)
