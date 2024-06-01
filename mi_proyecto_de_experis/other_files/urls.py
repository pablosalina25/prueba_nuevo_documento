from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.subir_archivos, name='subir_archivos'),
    path('subida_exitosa/', views.subida_exitosa, name='subida_exitosa'),
]