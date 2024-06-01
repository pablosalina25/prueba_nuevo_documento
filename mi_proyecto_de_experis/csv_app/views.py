# Create your views here.
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import os

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.size > 2097152:  # 2MB in bytes
                return render(request, 'csv_app/error.html', {'error_message': 'El archivo es demasiado grande. Debe ser menor a 2MB.'})
            if not file.name.endswith('.csv'):
                return render(request, 'csv_app/error.html', {'error_message': 'El archivo no es un archivo CSV válido.'})
            form.save()
            return redirect('csv_success')
    else:
        form = CSVUploadForm()
    return render(request, 'csv_app/upload.html', {'form': form})

def csv_success(request):
    return render(request, 'csv_app/success.html')
