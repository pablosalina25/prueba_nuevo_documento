from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.subir_documento, name='subir_documento'),
    path('exito/', views.exito, name='exito'),
    path('', views.inicio, name='inicio'),
]
