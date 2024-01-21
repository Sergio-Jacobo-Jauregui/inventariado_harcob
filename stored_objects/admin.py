from django.contrib import admin
from .models import StoredObjects

class StoredObjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount', 'organization', 'work', 'created_at', 'updated_at')

admin.site.register(StoredObjects, StoredObjectsAdmin)
 
