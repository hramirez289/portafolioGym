from django.urls import path
from .views import index, registro, contacto

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto")
]