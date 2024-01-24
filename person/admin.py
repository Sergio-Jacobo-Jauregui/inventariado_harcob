from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_names', 'last_names', 'dni', 'organization')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('organization')

admin.site.register(Person, PersonAdmin)
