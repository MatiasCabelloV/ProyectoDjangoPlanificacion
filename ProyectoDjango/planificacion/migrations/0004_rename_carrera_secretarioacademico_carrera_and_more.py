# Generated by Django 4.2.6 on 2023-11-01 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0003_remove_curso_administrador_remove_curso_aulas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secretarioacademico',
            old_name='Carrera',
            new_name='carrera',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='planificacionAcademica',
        ),
        migrations.AddField(
            model_name='planificacionacademica',
            name='curso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='planificacion.curso'),
        ),
        migrations.DeleteModel(
            name='HorarioCurso',
        ),
    ]
