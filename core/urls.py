from django.urls import path
from .views import index, registro, contacto, seleccionar_plan,  mi_espacio, panel_admin

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto"),
    path('planes/<str:plan_nombre>/<int:precio>/', seleccionar_plan, name='seleccionar_plan'),
    path('mi-espacio/', mi_espacio, name='mi_espacio'),
    path('admin-panel/', panel_admin, name='panel_admin'),

]
