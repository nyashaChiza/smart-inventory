from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer_name','total', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ['title', 'customer_name']
    inlines = [InvoiceItemInline]
    def total(self, obj):
        return sum(item.sub_total() for item in obj.invoice_items.all() )

    total.short_description = 'Total'


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity', 'unit_price', 'sub_total')
    list_filter = ('invoice__title', 'product')
    search_fields = ['invoice__title', 'product__product_name']

    def sub_total(self, obj):
        return obj.sub_total()

    sub_total.short_description = 'Sub Total'

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
