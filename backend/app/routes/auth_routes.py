from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth_schema import UserRegister, UserLogin
from app.services.auth_service import register_user, login_user
from app.database import get_db

router = APIRouter()

@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):
    user = register_user(db, data)
    return {"id": user.id, "email": user.email}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, data)
    return {"access_token": token}