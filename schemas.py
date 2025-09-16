from pydantic import BaseModel
from typing import Optional

# Base schema for ClassRoom
class ClassRoomBase(BaseModel):
    class_name: str
    class_teacher: str

# Schema for creating a new classroom
class ClassRoomCreate(ClassRoomBase):
    pass

# Schema for updating a classroom
class ClassRoomUpdate(BaseModel):
    class_name: Optional[str] = None
    class_teacher: Optional[str] = None

# Schema for returning classroom data
class ClassRoom(ClassRoomBase):
    id: int
    
    class Config:
        from_attributes = True
