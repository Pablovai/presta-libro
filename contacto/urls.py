from django.urls import path
from .import views

urlpatterns = [
 
    path('contacto_principal/', views.contacto_principal, name="contacto_principal"),
    
]