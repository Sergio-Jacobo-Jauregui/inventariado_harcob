from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, LogoutView

def ok(request):
    data = {'mensaje': 'All ok'}
    return JsonResponse(data)

urlpatterns = [
    path('ok/', ok),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('work/', include('work.urls')),
    path('stored_objects/', include('stored_objects.urls')),
]
