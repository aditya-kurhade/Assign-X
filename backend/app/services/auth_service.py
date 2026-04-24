from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.core.security import hash_password, verify_password, create_token

def register_user(db: Session, data):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email exists")

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(db: Session, data):
    user = db.query(User).filter(User.email == data.email).first()

    # if not user or not verify_password(data.password, user.password):
    #     raise HTTPException(401, "Invalid credentials")

    return create_token({"id": user.id, "role": user.role})