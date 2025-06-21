# FastAPI TODO API

Este es un proyecto base de una API de tareas (TODO) usando FastAPI.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload
```

## Endpoints

- `GET /`  
  Mensaje de bienvenida.
- `POST /todos`  
  Crea una nueva tarea.
- `GET /todos`  
  Lista todas las tareas.
- `GET /todos/{todo_id}`  
  Obtiene una tarea por su ID.
