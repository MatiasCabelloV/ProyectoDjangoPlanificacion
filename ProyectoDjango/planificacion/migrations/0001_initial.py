# Generated by Django 4.2.6 on 2023-10-20 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanificacionAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programa', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
                ('periodo', models.CharField(max_length=255)),
                ('jornada', models.CharField(max_length=255)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SecretarioAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carrera', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
