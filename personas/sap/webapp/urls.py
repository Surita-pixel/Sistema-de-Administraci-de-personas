from django.urls import path

from webapp.views import bienvenida

urlpatterns= [
    path('', bienvenida, name='index'),
]