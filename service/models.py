from django.db import models
from django.contrib.auth.models import User

class SolicitudServicio(models.Model):
    usuario = models.ForeignKey(
        User,  
        on_delete=models.CASCADE,
        verbose_name="Usuario",
        help_text="Introduce el usuario asignado.",
        null=True,
        blank=True,
    )
    fecha_solicitud = models.DateField()
    nombre = models.CharField(
        max_length=100,
        verbose_name="Título de la solicitud",
        help_text="Introduce que solicita.",
        null=True,
        blank=True,
    )
    descripcion = models.CharField(
        max_length=300,
        verbose_name="Descripcion",
        help_text="Introduce lo que busca.",
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to="solicitudes/",
        verbose_name="Imagen",
        help_text="Sube una imagen.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Título: {self.nombre}: Descripción: {self.descripcion}'
