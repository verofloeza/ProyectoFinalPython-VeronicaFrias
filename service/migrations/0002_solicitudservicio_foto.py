# Generated by Django 5.1.4 on 2024-12-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudservicio',
            name='foto',
            field=models.ImageField(blank=True, help_text='Sube una imagen.', null=True, upload_to='solicitudes/', verbose_name='Imagen'),
        ),
    ]
