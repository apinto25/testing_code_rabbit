from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

todos: Dict[int, dict] = {}
todo_id_counter = 1

class Todo(BaseModel):
    title: str
    description: str = None
    completed: bool = False

@app.get("/")
async def root():
    return {"message": "API TODO"}

@app.post("/todos")
async def create_todo(todo: Todo):
    global todo_id_counter
    todos[todo_id_counter] = todo.model_dump()
    response = {"id": todo_id_counter, **todo.model_dump()}
    todo_id_counter += 1
    return response

@app.get("/todos")
async def get_todos():
    return todos

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"id": todo_id, **todos[todo_id]}
