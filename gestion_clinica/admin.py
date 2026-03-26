from django.contrib import admin
# Importamos tus modelos
from .models import Paciente, Doctor, CitaMedica

# Los registramos para que aparezcan en el panel
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(CitaMedica)