# 🚍 SITU - Sistema Integrado de Transporte Urbano

Panel de administración web para la gestión del **Sistema Integrado de Transporte Urbano** de la ciudad de **Loja, Ecuador**.

## ✨ Funcionalidades

- **Pasajeros** — Registro, edición, eliminación y búsqueda de pasajeros con foto.
- **Tarjetas** — Gestión de tarjetas de acceso contactless asociadas a pasajeros.
- **Buses** — Administración de la flota: placa, cooperativa y número de unidad.
- **Viajes** — Registro de viajes con costo, cantidad, tipo de confort y fecha.
- **Simular Pago** — Simulador del lector de tarjetas a bordo del bus.
- **Historial** — Consulta del historial de viajes por pasajero.

## 🛠️ Stack tecnológico

| Capa        | Tecnología                           |
|-------------|--------------------------------------|
| Backend     | Python + Django                      |
| Base de datos | SQLite                            |
| Frontend    | HTML5, CSS3, Bootstrap 4.5, JS       |
| Imágenes    | Pillow                               |

## 🚀 Ejecución local

```bash
# Clonar el repositorio
git clone <repo-url>
cd ProyectoSITU

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver
```

Abrir [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📁 Estructura del proyecto

```
ProyectoSITU/
├── ProyectoSITU/          # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── appSITUweb/            # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas (CRUD + simulación)
│   ├── forms.py           # Formularios con validación
│   ├── admin.py
│   └── migrations/
├── templates/             # Plantillas HTML
│   ├── base.html          # Layout principal con sidebar
│   ├── index.html         # Dashboard
│   ├── pasajeros.html     # Listado de pasajeros
│   ├── tarjetas.html      # Listado de tarjetas
│   ├── buses.html         # Listado de buses
│   ├── viajes.html        # Listado de viajes
│   └── static/            # CSS, imágenes
├── manage.py              # Punto de entrada Django CLI
├── requirements.txt       # Dependencias Python
└── db.sqlite3             # Base de datos SQLite
```
