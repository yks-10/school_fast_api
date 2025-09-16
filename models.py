from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ClassRoom(Base):
    __tablename__ = "classrooms"
    
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False, index=True)
    class_teacher = Column(String, nullable=False)
    students = relationship("Student", back_populates="classroom")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    classroom = relationship("ClassRoom", back_populates="students")