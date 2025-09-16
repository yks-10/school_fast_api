from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import ClassRoom
from schemas import ClassRoomCreate, ClassRoomUpdate, ClassRoom as ClassRoomSchema

router = APIRouter(
    prefix="/classrooms",
    tags=["classrooms"]
)

@router.get("/", response_model=List[ClassRoomSchema])
def get_classrooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all classrooms with pagination"""
    classrooms = db.query(ClassRoom).offset(skip).limit(limit).all()
    return classrooms

@router.get("/{classroom_id}", response_model=ClassRoomSchema)
def get_classroom(classroom_id: int, db: Session = Depends(get_db)):
    """Get a specific classroom by ID"""
    classroom = db.query(ClassRoom).filter(ClassRoom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found"
        )
    return classroom

@router.post("/", response_model=ClassRoomSchema, status_code=status.HTTP_201_CREATED)
def create_classroom(classroom_data: ClassRoomCreate, db: Session = Depends(get_db)):
    """Create a new classroom"""
    # Check if classroom name already exists
    existing_classroom = db.query(ClassRoom).filter(ClassRoom.class_name == classroom_data.class_name).first()
    if existing_classroom:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Classroom with this name already exists"
        )
    
    db_classroom = ClassRoom(**classroom_data.dict())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

@router.put("/{classroom_id}", response_model=ClassRoomSchema)
def update_classroom(classroom_id: int, classroom_data: ClassRoomUpdate, db: Session = Depends(get_db)):
    """Update a classroom"""
    classroom = db.query(ClassRoom).filter(ClassRoom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found"
        )
    
    # Check if new classroom name already exists (if being updated)
    if classroom_data.class_name and classroom_data.class_name != classroom.class_name:
        existing_classroom = db.query(ClassRoom).filter(ClassRoom.class_name == classroom_data.class_name).first()
        if existing_classroom:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Classroom with this name already exists"
            )
    
    # Update only provided fields
    update_data = classroom_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(classroom, field, value)
    
    db.commit()
    db.refresh(classroom)
    return classroom

@router.delete("/{classroom_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_classroom(classroom_id: int, db: Session = Depends(get_db)):
    """Delete a classroom"""
    classroom = db.query(ClassRoom).filter(ClassRoom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found"
        )
    
    db.delete(classroom)
    db.commit()
    return None
