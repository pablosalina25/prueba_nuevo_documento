from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.upload_csv, name='upload_csv'),
    path('exito/', views.csv_success, name='csv_success'),
]
