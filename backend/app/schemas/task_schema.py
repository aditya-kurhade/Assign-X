from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    assign_to: int

class TaskUpdate(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    assigned_to: int