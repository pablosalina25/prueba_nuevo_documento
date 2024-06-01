from django.shortcuts import render, redirect
from .forms import ArchivoForm

def subir_archivos(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivos = request.FILES.getlist('archivo')
            if len(archivos) <= 50:
                for archivo in archivos:
                    nuevo_form = ArchivoForm({'archivo': archivo})
                    if nuevo_form.is_valid():
                        nuevo_form.save()
                return redirect('subida_exitosa')
            else:
                form.add_error(None, 'Solo se permite la carga de hasta 50 archivos a la vez.')
    else:
        form = ArchivoForm()

    return render(request, 'other_files/subir_archivos.html', {'form': form})

def subida_exitosa(request):
    return render(request, 'other_files/subida_exitosa.html')
