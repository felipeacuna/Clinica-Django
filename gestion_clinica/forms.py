from django import forms
from .models import Paciente, Doctor, CitaMedica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # Eliminamos 'fecha_nacimiento' y dejamos los campos reales del modelo
        fields = ['nombre', 'apellido', 'email', 'edad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['paciente', 'doctor', 'fecha_cita', 'motivo']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }