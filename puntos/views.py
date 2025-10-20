from django.shortcuts import render, redirect, get_object_or_404
from .models import Ubicacion
from django.http import HttpResponse

# Create your views here.

def index(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'puntos/index.html', {'ubicaciones': ubicaciones})

def crear_ubicacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        # Crear y guardar el objeto
        Ubicacion.objects.create(nombre=nombre, latitud=latitud, longitud=longitud)
        return redirect('index')
    return render(request, 'puntos/crear_ubicacion.html')

def editar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.nombre = request.POST.get('nombre')
        ubicacion.latitud = request.POST.get('latitud')
        ubicacion.longitud = request.POST.get('longitud')
        ubicacion.save()
        return redirect('index')
    return render(request, 'puntos/editar_ubicacion.html', {'ubicacion': ubicacion})

def eliminar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('index')
    return render(request, 'puntos/eliminar_ubicacion.html', {'ubicacion': ubicacion})
