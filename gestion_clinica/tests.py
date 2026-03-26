from django.test import TestCase
from .models import Paciente, Doctor
from django.core.exceptions import ValidationError

class ClinicaSistemaTest(TestCase):

    def setUp(self):
        # 1. Creamos datos iniciales para las pruebas
        # Estos datos solo viven mientras se ejecutan los tests
        self.doc_especialista = Doctor.objects.create(
            nombre="Dencil", 
            especialidad="Medicina General",
            registro_medico="MED-123"
        )
        
        self.paciente_1 = Paciente.objects.create(
            nombre="Felipe", 
            apellido="Acuña", 
            email="felipe@test.com", 
            edad=34
        )
        
        Paciente.objects.create(
            nombre="Javiera", 
            apellido="Perez", 
            email="javiera@test.com", 
            edad=28
        )

    # --- TEST DE CRUD Y DATOS ---
    def test_verificar_datos_creados(self):
        """Prueba que los datos del setUp se guardaron correctamente"""
        cantidad_pacientes = Paciente.objects.count()
        self.assertEqual(cantidad_pacientes, 2)
        self.assertEqual(self.doc_especialista.nombre, "Dencil")

    # --- TEST DE FILTROS ORM (Punto 2 de la evaluación) ---
    def test_filtro_orm_busqueda(self):
        """Prueba que el filtro icontains del ORM funciona"""
        # Buscamos "Fel" (debería encontrar a Felipe)
        resultado = Paciente.objects.filter(nombre__icontains="Fel")
        self.assertEqual(resultado.count(), 1)
        self.assertEqual(resultado[0].nombre, "Felipe")

    # --- TEST DE VALIDACIONES (Punto 6: a lo menos 3 validaciones) ---
    
    def test_validacion_edad_negativa(self):
        """Validación 1: La edad no puede ser menor a 0"""
        p_error = Paciente(nombre="Error", apellido="Test", email="e@t.com", edad=-1)
        with self.assertRaises(ValidationError):
            p_error.full_clean()

    def test_validacion_nombre_corto(self):
        """Validación 2: El nombre debe tener al menos 2 caracteres"""
        p_corto = Paciente(nombre="A", apellido="Test", email="a@t.com", edad=20)
        with self.assertRaises(ValidationError):
            p_corto.full_clean()

    def test_validacion_email_unico(self):
        """Validación 3: No pueden existir dos pacientes con el mismo email"""
        # Intentamos crear uno con el mismo email que self.paciente_1
        p_duplicado = Paciente(nombre="Clon", apellido="Test", email="felipe@test.com", edad=25)
        with self.assertRaises(ValidationError):
            p_duplicado.full_clean()