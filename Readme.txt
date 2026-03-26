# 🏥 VitalCare: Sistema de Gestión Clínica

¡Bienvenido a **VitalCare**! 

---

## 🌟 Propósito del Proyecto
VitalCare permite a centros médicos gestionar de forma integral el ciclo de atención: desde el registro administrativo de pacientes y el cuerpo médico, hasta el agendamiento inteligente de citas. El sistema asegura la persistencia de datos mediante una arquitectura relacional sólida, eliminando la redundancia y mejorando la trazabilidad de las consultas.

---

## 🚀 Stack Tecnológico

Este ecosistema fue construido utilizando un stack moderno, escalable y profesional:

* **Backend:** [Python](https://www.python.org/) + [Django 6.0](https://www.djangoproject.com/) (Framework de alto nivel para un desarrollo limpio y seguro).
* **Base de Datos:** [PostgreSQL](https://www.postgresql.org/) (Motor de base de datos relacional de grado empresarial).
* **Frontend:** HTML5, CSS3 y [Bootstrap 5](https://getbootstrap.com/) (Interfaz responsiva y moderna).
* **Entorno de Desarrollo:** Virtualenv (Encapsulamiento de dependencias).

---

## 🛠️ Estructura del Proyecto

El sistema sigue los estándares de la industria para facilitar el mantenimiento y la escalabilidad:

- `gestion_clinica/`: Lógica de negocio (Modelos de Pacientes, Doctores y Citas Médicas).
- `vitalcare_project/`: Configuración central del servidor, seguridad y enrutamiento principal.
- `templates/`: Capa de presentación visual (UI/UX) organizada por módulos.
- `vital_entorno/`: Entorno virtual dedicado para la gestión aislada de librerías.
- `manage.py`: Herramienta de administración y ejecución de comandos del proyecto.

---

## 📋 Funcionalidades Clave

1.  **Panel de Control Centralizado:** Acceso intuitivo a todas las áreas de gestión mediante tarjetas de navegación.
2.  **Gestión de Entidades:** Registro, edición y listado de Pacientes y Cuerpo Médico con validación de datos.
3.  **Sistema de Agendamiento:** Vinculación relacional dinámica entre pacientes y especialistas médicos.
4.  **Admin de Django Personalizado:** Interfaz avanzada para la supervisión, auditoría y gestión de registros por parte del administrador.
5.  **Seguridad y Sesiones:** Sistema de autenticación que protege las rutas sensibles de la clínica.

