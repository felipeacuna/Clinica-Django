from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente, Doctor, CitaMedica
from .forms import PacienteForm, DoctorForm, CitaMedicaForm

# --- VISTA PRINCIPAL ---

@login_required
def panel_control(request):
    """Renderiza el menú principal del sistema"""
    return render(request, 'gestion_clinica/panel.html')

# --- GESTIÓN DE PACIENTES ---

@login_required
def listar_pacientes(request):
    # Capturamos lo que el usuario escribe en un buscador de Bootstrap
    busqueda = request.GET.get('buscar')
    
    if busqueda:
        # FILTRO ORM: Buscamos coincidencias (icontains es "que contenga", no sensible a mayúsculas)
        pacientes = Paciente.objects.filter(nombre__icontains=busqueda)
    else:
        # Traer todos si no hay búsqueda
        pacientes = Paciente.objects.all()
        
    return render(request, 'gestion_clinica/pacientes_list.html', {'pacientes': pacientes})

@login_required
def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'gestion_clinica/paciente_form.html', {'form': form, 'titulo': 'Registrar Paciente'})

@login_required
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'gestion_clinica/paciente_confirm_delete.html', {'objeto': paciente})

def editar_paciente(request, pk):
    # Buscamos al paciente por su ID (Primary Key). Si no existe, da error 404.
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        # Pasamos los datos del POST y la instancia actual para que Django sepa qué editar
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'gestion_clinica/paciente_form.html', {'form': form, 'titulo': 'Editar Paciente'})

# --- GESTIÓN DE DOCTORES ---

@login_required
def listar_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'gestion_clinica/doctores_list.html', {'doctores': doctores})

@login_required
def editar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'gestion_clinica/doctor_form.html', {'form': form, 'titulo': 'Editar Doctor'})

def eliminar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('listar_doctores')
    return render(request, 'gestion_clinica/doctor_confirm_delete.html', {'objeto': doctor})

# --- GESTIÓN DE HORAS MÉDICAS ---

@login_required
def listar_horas(request):
    horas = CitaMedica.objects.all()
    return render(request, 'gestion_clinica/horas_list.html', {'horas': horas})

@login_required
def registrar_hora(request):
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_horas')
    else:
        form = CitaMedicaForm()
    return render(request, 'gestion_clinica/hora_form.html', {'form': form, 'titulo': 'Agendar Hora'})

@login_required
def modificar_hora(request, id):
    cita = get_object_or_404(CitaMedica, id=id)
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_horas')
    else:
        form = CitaMedicaForm(instance=cita)
    return render(request, 'gestion_clinica/hora_form.html', {'form': form, 'titulo': 'Modificar Hora'})

@login_required
def eliminar_hora(request, id):
    cita = get_object_or_404(CitaMedica, id=id)
    cita.delete()
    return redirect('listar_horas')

# --- VISTAS DE CREACIÓN (CREATE) ---

def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')
    else:
        form = DoctorForm()
    return render(request, 'gestion_clinica/doctor_form.html', {
        'form': form, 
        'titulo': 'Registrar Nuevo Médico'
    })

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'gestion_clinica/paciente_form.html', {
        'form': form, 
        'titulo': 'Registrar Nuevo Paciente'
    })