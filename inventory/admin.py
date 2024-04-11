from .models import Stock
from .models import Category
from django.contrib import admin
from .models import StockMovement



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated')
    ordering = ('-created',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'price', 'category', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated', 'category')
    ordering = ('-created',)



@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'movement_quantity', 'previous_quantity', 'current_quantity', 'movement_type', 'price', 'stock', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('movement_type', 'created', 'updated')
    ordering = ('-created',)

