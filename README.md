# 🏥 VitalCare - Sistema de Gestión Clínica

**VitalCare** es una plataforma de gestión para instituciones de salud, desarrollada como parte de la evaluación final del módulo de **Django** en el Bootcamp Full Stack Python. 

El proyecto integra un sistema de administración robusto con una base de datos **PostgreSQL**, permitiendo la gestión eficiente de pacientes, doctores y citas médicas bajo una interfaz moderna y responsiva.

---

## 🚀 Características Principales (Requerimientos)

Este proyecto cumple con los siguientes puntos técnicos evaluados:

1.  **Arquitectura MVT**: Implementación completa de Modelos, Vistas y Templates.
2.  **Base de Datos Relacional**: Conectado a **PostgreSQL** para la persistencia de datos.
3.  **CRUD Completo**: Gestión total (Crear, Leer, Actualizar, Borrar) de pacientes y personal médico.
4.  **Filtros ORM**: Buscador inteligente que utiliza filtros avanzados del ORM de Django (`icontains`).
5.  **Interfaz Bootstrap**: Diseño 100% responsivo y profesional utilizando componentes de Bootstrap 5.
6.  **Validaciones y Tests**: Cobertura de pruebas unitarias (`TestCase`) asegurando la integridad de los datos (edad, nombres y correos únicos).
7.  **Seguridad**: Uso de decoradores `@login_required` para proteger la información sensible.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.14
* **Framework:** Django 5.x / 6.0
* **Base de Datos:** PostgreSQL
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Entorno Virtual:** venv

---

## 📂 Estructura del Proyecto

* `vitalcare_project/`: Configuración principal del proyecto Django.
* `gestion_clinica/`: Aplicación principal que contiene la lógica de la clínica.
    * `models.py`: Definición de Pacientes, Doctores y Citas.
    * `views.py`: Lógica de negocio y filtros ORM.
    * `forms.py`: Formularios con validaciones personalizadas.
    * `tests.py`: Suite de pruebas unitarias.
* `templates/`: Plantillas base y específicas de la aplicación.

---

## ⚙️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/Entorno_Vital.git](https://github.com/tu-usuario/Entorno_Vital.git)
    cd Entorno_Vital
    ```

2.  **Activar Entorno Virtual:**
    ```bash
    .\vital_entorno\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install django psycopg2
    ```

4.  **Configurar Base de Datos:**
    Asegúrate de tener PostgreSQL corriendo y configurar las credenciales en `settings.py`. Luego ejecuta:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Ejecutar el Servidor:**
    ```bash
    python manage.py runserver
    ```

---

## 🧪 Pruebas Unitarias

Para verificar la integridad del sistema y las validaciones de modelos:
```bash
python manage.py test gestion_clinica
