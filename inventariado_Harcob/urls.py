from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def ok(request):
    data = {'mensaje': 'All ok'}
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('ok/', ok),
    path('orgs/', include('organization.urls')),
]
