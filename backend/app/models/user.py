from sqlalchemy import Column, Integer, String
from app.database.connection import base

class User(base):
    __tablename__: "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(string(100), unique=True)
    password = Colume(String(225))
    role = Column(String(20))

