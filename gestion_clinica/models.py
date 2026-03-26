from django.db import models
from django.core.exceptions import ValidationError

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Añadimos null=True (para la BD) y blank=True (para el formulario)
    email = models.EmailField(unique=True, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)

    def clean(self):
        # Mantenemos tus validaciones para el Punto 6 (Tests)
        if self.edad is not None and self.edad < 0:
            raise ValidationError('La edad no puede ser negativa.')
        if len(self.nombre) < 2:
            raise ValidationError('El nombre es demasiado corto.')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    # Le quitamos el unique=True y añadimos null=True, blank=True
    registro_medico = models.CharField(max_length=20, null=True, blank=True) 

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad}"

class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    motivo = models.TextField()