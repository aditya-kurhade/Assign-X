from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskCreate
from app.services.task_service import create_task, get_tasks
from app.dependencies.db_dependency import get_db
from app.dependencies.auth_dependency import get_current_user
from app.dependencies.role_checker import require_manager

router = APIRouter()

@router.post("/")
def create(data: TaskCreate,
           db: Session = Depends(get_db),
           user=Depends(get_current_user)):
    
    require_manager(user)
    return create_task(db, data, user)


@router.get("/")
def list_tasks(db: Session = Depends(get_db),
               user=Depends(get_current_user)):
    
    return get_tasks(db, user)