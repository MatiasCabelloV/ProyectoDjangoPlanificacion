from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SecretarioAcademico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=255)

    def __str__ (self):
        return self.user

class PlanificacionAcademica(models.Model):
    programa = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    jornada = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

class Curso(models.Model):
    planificacionAcademica = models.ForeignKey(PlanificacionAcademica, on_delete=models.CASCADE)
    facultad = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    unidadAcademica = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    Curso = models.CharField(max_length=255)
    seccion = models.CharField(max_length=10)
    jornada = models.CharField(max_length=20)
    nrc = models.CharField(max_length=20)
    listaCruzada = models.CharField(max_length=255)
    nrcLigados = models.CharField(max_length=255)
    idListaCurzada = models.IntegerField()
    calificable = models.IntegerField()
    minor = models.IntegerField()
    nombreAsignatura = models.CharField(max_length=255)
    horasAPagar = models.IntegerField()
    tipoActividad = models.CharField(max_length=255)
    modalidad = models.CharField(max_length=20)
    numeroVacantes = models.IntegerField()
    numeroInscritos = models.IntegerField()
    restriccionCodPrograma = models.CharField(max_length=255)
    restriccionDescPrograma = models.CharField(max_length=255)
    restriccionCampus = models.CharField(max_length=255)
    nivelCurso = models.IntegerField()
    unidadQuePaga = models.CharField(max_length=255)
    semestreQuePaga = models.CharField(max_length=20)
    prorcentajeOnline = models.FloatField()
    proveedor = models.CharField(max_length=255)
    administrador = models.CharField(max_length=255)
    iniciativa = models.CharField(max_length=255)
    aulas = models.CharField(max_length=255)

class HorarioCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    horaInicio = models.CharField(max_length=255)
    horaFin = models.CharField(max_length=255)
    dia = models.CharField(max_length=255)