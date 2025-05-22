# FastAPI CRUD + Comentarios Inteligentes

API RESTful con FastAPI para gestión de items y análisis inteligente de comentarios.

## 📌 Descripción

Este proyecto implementa una API RESTful usando FastAPI que permite gestionar items con operaciones CRUD y manejar comentarios con análisis inteligente. Los comentarios son clasificados, analizados por sentimiento, y almacenados en PostgreSQL a través de Supabase. Se utiliza SQLAlchemy como ORM y Pydantic para validaciones.

## 🌍 Tecnologías Usadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- Uvicorn
- Pydantic v2

## 🔧 Instalación Local

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/fastapi-crud-comments.git
cd fastapi-crud-comments
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Mac/Linux
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno en un archivo `.env`:
```
DATABASE_URL=postgresql://postgres.ltgofrkdsrwctojsspuq:Val724148@aws-0-us-east-2.pooler.supabase.com:6543/postgres
```

5. Inicia el servidor:
```bash
uvicorn app.main:app --reload
```

6. Accede a la documentación interactiva:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📝 Endpoints Implementados

### 🔢 /items

| Método | Ruta          | Descripción              |
|--------|---------------|--------------------------|
| POST   | /items        | Crear nuevo item         |
| GET    | /items/{id}   | Obtener item por ID      |
| PUT    | /items/{id}   | Actualizar item por ID   |
| DELETE | /items/{id}   | Eliminar item por ID     |

### 💬 /comments

| Método | Ruta               | Descripción                              |
|--------|--------------------|------------------------------------------|
| POST   | /comments          | Crear comentario con análisis            |
| GET    | /comments/{id}     | Leer comentario por ID                   |
| GET    | /comments          | Listar todos los comentarios             |
| GET    | /comments-stats    | Ver estadísticas globales de comentarios|

## 🏢 Estructura del Proyecto

```
fastapi-crud-comments/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── comments/
│   │   ├── crud.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── schemas.py
├── .env
├── requirements.txt
└── README.md
```

## 🌟 Características Destacadas

- Modularización con routers independientes
- Clasificación automática de comentarios (aprobado / rechazado)
- Análisis de sentimiento (positivo, negativo, neutral)
- Estadísticas generales de comentarios

## 🚀 Futuras Mejoras

- Autenticación de usuarios
- Paginación de comentarios
- Exportación de datos a CSV

## 👤 Autor

Desarrollado por Laura
