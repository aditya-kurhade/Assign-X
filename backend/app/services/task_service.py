from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, data, user):
    task = Task(
        title=data.title,
        description=data.description,
        assigned_to=data.assigned_to,
        created_by=user["id"]
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session, user):
    if user["role"] == "manager":
        return db.query(Task).all()
    return db.query(Task).filter(Task.assigned_to == user["id"]).all()