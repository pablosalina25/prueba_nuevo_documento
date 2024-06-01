from django.urls import path, include
from archivos_pdf import views as pdf_views
from csv_app import views as csv_views

urlpatterns = [
    path('', pdf_views.inicio, name='inicio'),
    path('subir_pdf/', pdf_views.subir_documento, name='subir_documento_pdf'),
    path('subir_csv/', csv_views.upload_csv, name='subir_documento_csv'),
    path('exito/', pdf_views.exito, name='exito'),
]
