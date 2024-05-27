from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['archivo']

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')

        # Verificar que el archivo es un PDF
        if not archivo.name.endswith('.pdf'):
            raise forms.ValidationError('El archivo debe ser unicamente en formato PDF.')

        # Verificar el tamaño del archivo
        if archivo.size > 2 * 1024 * 1024:  # 2 MB
            raise forms.ValidationError('El archivo no debe superar los 2 MB.')

        return archivo
