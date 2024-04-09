from django.contrib import admin
from .models import Integration

class IntegrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'host', 'source', 'created', 'updated')
    search_fields = ('username', 'host')
    list_filter = ('source', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    fieldsets = (
        ('Integration Details', {
            'fields': ('username', 'password', 'host', 'key', 'endpoint', 'source')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )
    actions = ['test_connection']

    def test_connection(self, request, queryset):
        # Implement your logic to test the connection for selected Integration objects
        pass
    test_connection.short_description = "Test Connection"

admin.site.register(Integration, IntegrationAdmin)