from django.urls import path
from . import views

urlpatterns = [
    path('for_org/', views.get_for_org),
]
