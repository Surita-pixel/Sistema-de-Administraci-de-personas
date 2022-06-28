from django.shortcuts import render, get_object_or_404, redirect
from personas.models import Domicilio
from .forms import DomicilioForm

def homeDomicilios(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'home.html', {'no_domicilios': no_domicilios, 'domicilios':domicilios})

def getDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'detalledomicilio.html', {'domicilio': domicilio})

def createDomicilio(request):
    if request.method == "POST":
        formDomicilio = DomicilioForm(request.POST)
        if formDomicilio.is_valid():
            formDomicilio.save()
            return redirect('domicilios home')

    else:
        formDomicilio = DomicilioForm()
        return render(request, 'nuevo domicilio.html', {'formDomicilio': formDomicilio})
    return render(request, 'nuevo domicilio.html', {'formDomicilio': formDomicilio})

def deleteDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()

    return redirect('domicilios home')

