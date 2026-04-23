from sqlalchemy import Column, Integer, String
from app.database.connection import base

class Task(base):
    __tablename__: "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(225))
    assign_to = Column(Integer, ForeignKey="users.id")
    created_by = Column(Integer, ForeignKey="users.id")