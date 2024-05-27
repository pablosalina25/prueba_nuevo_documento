from django.shortcuts import render

# Create your views here.

from django.core.exceptions import ValidationError
from .forms import CSVUploadForm

def validate_csv(file):
    if not file.name.endswith('.csv'):
        raise ValidationError('El archivo no es un CSV')
    if file.size > 2 * 1024 * 1024:
        raise ValidationError('El archivo no debe superar los 2 MB')

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            try:
                validate_csv(file)
                
                return render(request, 'csv_checker/success.html')
            except ValidationError as e:
                form.add_error('file', e)
    else:
        form = CSVUploadForm()
    return render(request, 'csv_checker/upload.html', {'form': form})

