from django.urls import path
from . import views

urlpatterns = [
    # Ruta del Panel Principal (Dashboard)
    path('panel/', views.panel_control, name='panel_control'),

    # Rutas para PACIENTES (CRUD completo)
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/registro/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),

    # Rutas para DOCTORES (CRUD completo)
    path('doctores/', views.listar_doctores, name='listar_doctores'),
    path('doctores/registro/', views.registrar_doctor, name='registrar_doctor'),
    path('doctores/editar/<int:pk>/', views.editar_doctor, name='editar_doctor'),
    path('doctores/eliminar/<int:pk>/', views.eliminar_doctor, name='eliminar_doctor'),

    # Rutas para Horas Médicas
    path('horas/', views.listar_horas, name='listar_horas'),
    path('horas/registro/', views.registrar_hora, name='registrar_hora'),
    path('horas/eliminar/<int:id>/', views.eliminar_hora, name='eliminar_hora'),
    path('horas/modificar/<int:id>/', views.modificar_hora, name='modificar_hora'),

]