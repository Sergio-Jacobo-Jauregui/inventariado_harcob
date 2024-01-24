from django.contrib import admin
from .models import PurchaseRecord

class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'organization', 'work', 'stored_object', 'created_at', 'updated_at')
 
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('organization', 'work', 'stored_object')

admin.site.register(PurchaseRecord, PurchaseRecordAdmin)
