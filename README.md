# Tarea4_Programacion213023
- Tarea 4 de programación 

# Sistema de Gestión de Reservas

Sistema de escritorio desarrollado en Python usando Tkinter, Programación Orientada a Objetos (POO), arquitectura MVC y principios SOLID.

El proyecto permite gestionar:

- Clientes
- Servicios
- Reservas
- Dashboard dinámico
- Persistencia de datos en archivos JSON

---

# Características

## Gestión de Clientes
- Registro de clientes
- Persistencia en JSON
- Tabla dinámica

## Gestión de Servicios
- Registro de:
  - Asesorías
  - Salas
  - Equipos
- Cálculo automático de costos
- Persistencia en JSON

## Gestión de Reservas
- Crear reservas
- Confirmar reservas
- Cancelar reservas
- Relación entre clientes y servicios
- Persistencia en JSON

## Dashboard
- Estadísticas dinámicas
- Últimas reservas
- Indicadores visuales

---

# Tecnologías usadas

- Python 3
- Tkinter
- Pillow
- tkcalendar
- JSON

---

# Arquitectura del Proyecto

El proyecto implementa:

- Programación Orientada a Objetos (POO)
- Arquitectura MVC
- Principios SOLID
- Persistencia local con JSON

---

# Requisitos
- Python
- Instalar dependencias 
    Ejecutar: pip install -r requirements.txt

# Ejecucion
- Ejecutar el archivo principal:
    - python main.py
- Credenciales por defecto:
    - usuario: programacion
    - contraseña: programacion

# Estructura del Proyecto

```bash
project/
│
├── controllers/
├── models/
├── utils/
├── views/
│
├── data/
├── img/
│
├── main.py
├── logs.txt
├── requirements.txt
└── README.md