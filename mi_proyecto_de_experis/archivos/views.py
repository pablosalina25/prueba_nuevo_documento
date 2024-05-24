from django.shortcuts import render, redirect
from .forms import DocumentoForm

def subir_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = DocumentoForm()
    return render(request, 'archivos/subir_documento.html', {'form': form})

def exito(request):
    return render(request, 'archivos/exito.html')

def inicio(request):
    return render(request, 'archivos/inicio.html')


# Create your views here.
