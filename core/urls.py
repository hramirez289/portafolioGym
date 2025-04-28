from django.urls import path
from .views import index, registro, contacto, seleccionar_plan

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto"),
    path('planes/<str:plan_nombre>/<int:precio>/', seleccionar_plan, name='seleccionar_plan'),

]
