from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from personas.models import Persona
# Create your views here.
def bienvenida(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {"no_personas":no_personas, 'personas': personas})

