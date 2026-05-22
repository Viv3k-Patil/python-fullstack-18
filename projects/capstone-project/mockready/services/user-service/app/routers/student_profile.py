from uuid import UUID

from fastapi import APIRouter
from app.schemas.student_profile import StudentProfileCreate, StudentProfileUpdate
from app.services.student_profile_services import student_profile_service

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", status_code=201)
def add_student(data: StudentProfileCreate):
    return student_profile_service.create(data)

@router.get("/")
def list_students():
    return student_profile_service.get_all()

@router.get("/{student_id}")
def read_student(student_id: UUID):
    return student_profile_service.get_by_id(student_id)

@router.put("/{student_id}")
def edit_student(student_id: UUID, data: StudentProfileUpdate):
    return student_profile_service.update(student_id, data)

@router.delete("/{student_id}")
def remove_student(student_id: UUID):
    return student_profile_service.delete(student_id)