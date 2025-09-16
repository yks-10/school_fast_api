from sqlalchemy import Column, Integer, String
from database import Base

class ClassRoom(Base):
    __tablename__ = "classrooms"
    
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False, index=True)
    class_teacher = Column(String, nullable=False)
