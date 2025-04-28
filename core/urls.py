from django.urls import path
<<<<<<< HEAD
from .views import index

urlpatterns = [
    path('', index, name="index")
=======
from .views import index, registro, contacto

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto")
>>>>>>> 7bd92602f268b218a9574e8ccdae7d5ed7416467
]