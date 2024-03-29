from django.contrib import admin
from .models import StoredObjects

class StoredObjectsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'type', 'stored_quantity', 'quantity_in_use', 'organization', 'work', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('organization', 'work')

admin.site.register(StoredObjects, StoredObjectsAdmin)
 
