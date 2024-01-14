def ok(request):
    data = {'mensaje': 'All ok'}
    return JsonResponse(data)

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ok/', ok),
    path('orgs/', include('organization.urls')),
]
