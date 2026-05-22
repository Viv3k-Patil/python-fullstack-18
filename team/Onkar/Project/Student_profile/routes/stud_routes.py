from fastapi import APIRouter
from app.schema import StudentCreate, StudentUpdate
from app.services import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def add_student(data: StudentCreate):
    return create_student(data)

@router.get("/")
def list_students():
    return get_students()

@router.get("/{student_id}")
def read_student(student_id: int):
    return get_student(student_id)

@router.put("/{student_id}")
def edit_student(student_id: int, data: StudentUpdate):
    return update_student(student_id, data)

@router.delete("/{student_id}")
def remove_student(student_id: int):
    return delete_student(student_id)