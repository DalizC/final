from django.db import models
from django.utils import timezone
import datetime


class Perfil(models.Model):
    password = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Usuario(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=200)
    fono = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    perfil = models.ForeignKey(
        Perfil, on_delete=models.SET_NULL, default=None, null=True)

    class Meta:
        abstract = True


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class Medico(Usuario):

    especialidad = models.ForeignKey(
        Especialidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Dr/a. ' + self.nombres + '' + self.apellidos


class Paciente(Usuario):
    def __str__(self):
        return 'Sr/a/ita.' + self.nombres + '' + self.apellidos


class Agenda(models.Model):
    fecha = models.DateField()
    hora_desde = models.TimeField()
    hora_hasta = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.medico.nombres + self.medico.apellidos + ': ' + str(self.fecha) + ' ' + str(self.hora_desde) + ' - ' + str(self.hora_hasta)

    def is_expired(self):
        return self.fecha >= timezone.now().date - datetime.timedelta(days=1)


class Cita(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.SET_NULL, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.paciente.nombres + self.paciente.apellidos + ' ' + self.agenda.fecha + ' ' + self.agenda.hora_desde + ' - ' + self.agenda.hora_hasta + ' médico: ' + self.agenda.medico.apellidos
