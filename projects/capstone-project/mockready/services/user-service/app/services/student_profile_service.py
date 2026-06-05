"""
services/Student_Profile_Service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""


from uuid import UUID, uuid4
from datetime import datetime, timezone 
from app.schemas.student_profile import StudentProfileCreate, StudentProfileUpdate, StudentProfileResponse
from app.core.exceptions import NotFoundException, ConflictException
# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by Student_Profile_Repository in Phase 2.
# Do not add any logic that depends on this being a dict.
_student_profiles: dict[UUID, dict] = {}

class Student_Profile_Service:

    def create(self, data: StudentProfileCreate) -> StudentProfileResponse:

        for s in _student_profiles.values():
           if s["name"].lower() == data.name.lower():
                raise ConflictException(f"Student '{data.name}' already exists")



        student_profile = {
            "id": uuid4(),
            "user_id": data.user_id,
            "batch_id": data.batch_id,
            "enrollment_number": data.enrollment_number,
            "name": data.name,
            "city": data.city,
            "address": data.address,
            "skills": data.skills,
            "interests": data.interests,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }
        _student_profiles[student_profile["id"]] = student_profile
        return StudentProfileResponse(**student_profile)

    def get_all(self, page: int, size: int) -> tuple[list[StudentProfileResponse], int]:
        active = [s for s in _student_profiles.values() if s["is_active"]]
        total = len(active)
        start = (page - 1) * size
        chunk = active[start: start + size]
        return [StudentProfileResponse(**s) for s in chunk], total
    
    def get_by_id(self, student_id: UUID) -> StudentProfileResponse:
        student_profile = _student_profiles.get(student_id)
        if not student_profile or not student_profile["is_active"]:
            raise NotFoundException(f"Student profile {student_id} not found")
        return StudentProfileResponse(**student_profile)
    
    def update(self, student_id: UUID, data: StudentProfileUpdate) -> StudentProfileResponse:
        student_profile = _student_profiles.get(student_id)
        if not student_profile or not student_profile["is_active"]:
            raise NotFoundException(f"Student profile {student_id} not found")
        
        # business rule: no duplicate student names
        for s in _student_profiles.values():
            if s["id"] != student_id and s["name"].lower() == data.name.lower():
                raise ConflictException(f"Student '{data.name}' already exists")

        student_profile.update({
            "name": data.name,
            "city": data.city,
            "address": data.address,
            "skills": data.skills,
            "is_active": data.is_active
        })
        return StudentProfileResponse(**student_profile)
    
    def delete(self, student_id: UUID) -> None:
        student_profile = _student_profiles.get(student_id)
        if not student_profile or not student_profile["is_active"]:
            raise NotFoundException(f"Student profile {student_id} not found")
        student_profile["is_active"] = False

        return StudentProfileResponse(**student_profile)    


student_profile_service = Student_Profile_Service()



    
