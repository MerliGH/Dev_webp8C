
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pendiente
from .forms import PendienteForm
import os
from django.conf import settings
import json


def lista_pendientes(request):
    pendientes = Pendiente.objects.all()
    return render(request, 'pendientes/lista_pendientes.html', {'pendientes': pendientes})

def crear_pendiente(request):
    if request.method == 'POST':
        form = PendienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pendientes')
    else:
        form = PendienteForm()
    return render(request, 'pendientes/form_pendiente.html', {'form': form})

def editar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    if request.method == 'POST':
        form = PendienteForm(request.POST, instance=pendiente)
        if form.is_valid():
            form.save()
            return redirect('lista_pendientes')
    else:
        form = PendienteForm(instance=pendiente)
    return render(request, 'pendientes/form_pendiente.html', {'form': form})

def eliminar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    if request.method == 'POST':
        pendiente.delete()
        return redirect('lista_pendientes')
    return render(request, 'pendientes/eliminar_pendiente.html', {'pendiente': pendiente})




def cargar_pendientes_desde_json():
    ruta = os.path.join(settings.BASE_DIR, 'pendientes_data.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data





def lista_ids(request):
    pendientes = Pendiente.objects.all().values('id')
    return render(request, 'pendientes/solo_ids.html', {'pendientes': pendientes})

def lista_ids_titles(request):
    pendientes = Pendiente.objects.all().values('id', 'title')
    return render(request, 'pendientes/ids_titles.html', {'pendientes': pendientes})

def lista_sin_resolver(request):
    pendientes = Pendiente.objects.filter(completed=False).values('id', 'title')
    return render(request, 'pendientes/sin_resolver.html', {'pendientes': pendientes})

def lista_resueltos(request):
    pendientes = Pendiente.objects.filter(completed=True).values('id', 'title')
    return render(request, 'pendientes/resueltos.html', {'pendientes': pendientes})

def lista_ids_user(request):
    pendientes = Pendiente.objects.all().values('id', 'userId')
    return render(request, 'pendientes/ids_user.html', {'pendientes': pendientes})

def lista_resueltos_user(request):
    pendientes = Pendiente.objects.filter(completed=True).values('id', 'userId')
    return render(request, 'pendientes/resueltos_user.html', {'pendientes': pendientes})

def lista_sin_resolver_user(request):
    pendientes = Pendiente.objects.filter(completed=False).values('id', 'userId')
    return render(request, 'pendientes/sin_resolver_user.html', {'pendientes': pendientes})




def lista_pendientes_desde_json(request):
    ruta_json = os.path.join(settings.BASE_DIR, 'pendientes', 'data', 'pendientes.json')
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        pendientes = json.load(archivo)
    return render(request, 'pendientes/lista_desde_json.html', {'pendientes': pendientes})