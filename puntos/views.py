from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def ubicaciones(request):
    return HttpResponse("Bienvenido a ubicaciones")