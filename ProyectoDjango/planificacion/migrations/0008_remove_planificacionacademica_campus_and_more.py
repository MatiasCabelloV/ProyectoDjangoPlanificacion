# Generated by Django 4.2.6 on 2023-11-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0007_modulo_planificacionacademica_actividad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planificacionacademica',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='planificacionacademica',
            name='modulos',
        ),
        migrations.AddField(
            model_name='planificacionacademica',
            name='modulos',
            field=models.CharField(default='', max_length=255),
        ),
    ]
