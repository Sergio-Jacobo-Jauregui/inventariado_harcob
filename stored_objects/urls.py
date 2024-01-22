from django.urls import path
from . import views

urlpatterns = [
    path('for_work/', views.get_for_org),
    path('create/', views.create_stored_object),
]
