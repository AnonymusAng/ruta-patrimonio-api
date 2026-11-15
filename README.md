# Ruta Patrimonio API

API para el catálogo patrimonial, construida con Django REST Framework. Incluye los modelos `Categoria`, `Lugar` y `Evento`, sus relaciones, serializers, ViewSets, rutas CRUD y datos de demostración.

## Requisitos

- Python 3.11 o superior.
- Git instalado.

## Ejecutar en Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/demo.json
python manage.py runserver
```

La API queda disponible en `http://127.0.0.1:8000/api/`. Rutas: `/categorias/`, `/lugares/` y `/eventos/`. CORS ya permite los orígenes locales de Vite en el puerto 5173.

## Publicar en GitHub

Crea un repositorio vacío llamado `ruta-patrimonio-api`. Desde esta carpeta, configura tu identidad de Git y publica el código:

```powershell
git init -b main
git config user.name "Tu nombre completo"
git config user.email "correo vinculado a GitHub"
git add .
git status
git commit -m "chore(backend): inicia la API patrimonial"
git remote add origin https://github.com/USUARIO/ruta-patrimonio-api.git
git push -u origin main
```

Reemplaza `USUARIO` por el dueño del repositorio. Inicia sesión con tu propia cuenta de GitHub. El `.gitignore` excluye `.venv`, `db.sqlite3`, archivos `.env` y cachés.
