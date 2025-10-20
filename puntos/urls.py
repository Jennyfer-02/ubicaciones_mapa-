from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Listar ubicaciones
    path('crear/', views.crear_ubicacion, name='crear_ubicacion'),
    path('editar/<int:id>/', views.editar_ubicacion, name='editar_ubicacion'),
    path('eliminar/<int:id>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
]
