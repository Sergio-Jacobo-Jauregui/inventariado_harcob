from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_accion_record),
    path('for_work/', views.get_for_work),
]
