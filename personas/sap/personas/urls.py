from django.urls import path

from .views import detallePersona, nuevaPersona, editarPersona, eliminarPersona

urlpatterns = [
    path('detalle_persona/<int:id>', detallePersona, name='detail'),
    path('crear_persona/', nuevaPersona, name='new person'),
    path('editar_persona/<int:id>', editarPersona, name='edit'),
    path('eliminar_persona/<int:id>', eliminarPersona, name='delete'),

]