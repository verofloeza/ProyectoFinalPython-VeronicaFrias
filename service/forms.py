from django import forms
from service.models import SolicitudServicio
from django.contrib.auth.models import User

class SolicitudForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),  
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text='Requerido. Seleccione el usuario.'
    )
    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Requerido. Coloque un título.'
    )
    fecha_solicitud = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        help_text='Requerido. Seleccione una fecha.'
    )

    class Meta:
        model = SolicitudServicio
        fields = ['usuario', 'nombre', 'descripcion', 'fecha_solicitud', 'foto']