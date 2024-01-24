from django.contrib import admin
from .models import AccionRecord

class AccionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'quantity', 'quantity_type', 'organization', 'work', 'stored_object', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('organization', 'work', 'stored_object')

admin.site.register(AccionRecord, AccionRecordAdmin)
