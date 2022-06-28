from django.shortcuts import render, get_object_or_404, redirect

from .models import Persona
from personas.forms import personForm
# Create your views here.
def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona': persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == "POST":
        formPersona = personForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')
    else: 
        formPersona = personForm()
        return render(request, 'nuevo.html', {'formPersona': formPersona})
    
    return render(request, 'nuevo.html', {'formPersona': formPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        formPersona = personForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')
    else: 
        formPersona = personForm(instance=persona)
    
    return render(request, 'editar.html', {'formPersona': formPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')
