from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active', 'organization', 'created_at', 'updated_at')

admin.site.register(Work, WorkAdmin)
