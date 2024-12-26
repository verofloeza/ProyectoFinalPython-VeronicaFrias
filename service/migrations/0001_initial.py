# Generated by Django 5.1.4 on 2024-12-19 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('nombre', models.CharField(blank=True, help_text='Introduce que solicita.', max_length=100, null=True, verbose_name='Título de la solicitud')),
                ('descripcion', models.CharField(blank=True, help_text='Introduce lo que busca.', max_length=300, null=True, verbose_name='Descripcion')),
                ('usuario', models.ForeignKey(blank=True, help_text='Introduce el usuario asignado.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
