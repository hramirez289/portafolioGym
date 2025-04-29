from django.urls import path
from .views import index, registro, contacto, seleccionar_plan,  mi_espacio, panel_admin, eliminar_curso, editar_curso

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('contacto', contacto, name="contacto"),
    path('planes/<str:plan_nombre>/<int:precio>/', seleccionar_plan, name='seleccionar_plan'),
    path('mi-espacio/', mi_espacio, name='mi_espacio'),
    path('admin-panel/', panel_admin, name='panel_admin'),
    
    path('editar_curso/<int:curso_id>/', editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),

]
