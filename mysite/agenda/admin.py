from django.contrib import admin

from .models import Paciente, Medico, Especialidad, Agenda, Cita, Perfil

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(Perfil)
admin.site.register(Agenda)
admin.site.register(Cita)
