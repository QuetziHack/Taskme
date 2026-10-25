from fastapi import FastAPI
from schemas import Task
app = FastAPI()
tasks = []
@app.get("/")
def taskme():
    return {"mensaje": "taskme"}

@app.get("/createtask/{task}")
def create_task(task: str):
    return {"mensaje": "funcion en desarrollo",
            "task":task}
