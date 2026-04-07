from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title="Task Management API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}

@app.post("/tasks/")
def create_task(task: dict, db: Session = Depends(database.get_db)):
    db_task = models.Task(**task)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/")
def read_tasks(db: Session = Depends(database.get_db)):
    return db.query(models.Task).all()