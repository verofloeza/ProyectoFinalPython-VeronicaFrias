from django import forms
from service.models import SolicitudServicio
from django.contrib.auth.models import User

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['usuario', 'nombre', 'descripcion', 'fecha_solicitud', 'foto']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_solicitud': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'  # Solo acepta imágenes
            })
        }