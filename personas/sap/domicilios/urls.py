from django.urls import path

from .views import homeDomicilios, getDomicilio, createDomicilio, deleteDomicilio

urlpatterns = [
    path('domicilios/', homeDomicilios, name="domicilios home"),
    path('domicilios/detalle_domicilio/<int:id>', getDomicilio),
    path('domicilios/crear_domicilio', createDomicilio),
    path('domicilios/eliminar_domicilio/<int:id>', deleteDomicilio),
    
]