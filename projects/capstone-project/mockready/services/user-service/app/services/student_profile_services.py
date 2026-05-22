from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.student_profile import StudentProfileCreate, StudentProfileUpdate, StudentProfileResponse

_student_profiles = {}


class StudentProfileService:
    def create(self, data: StudentProfileCreate) -> StudentProfileResponse:
        sp = {
            "id": uuid4(),
            "full_name": data.full_name,
            "email": data.email,
            "phone": data.phone,
            "enrollment_number": data.enrollment_number,
            "skills": data.skills,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }
        _student_profiles[sp["id"]] = sp
        return StudentProfileResponse(**sp)

    def get_all(self):
        return [StudentProfileResponse(**sp) for sp in _student_profiles.values() if sp["is_active"]]

    def get_by_id(self, student_profile_id: UUID):
        return StudentProfileResponse(**_student_profiles[student_profile_id])

    def update(self, student_profile_id: UUID, data: StudentProfileUpdate):
        _student_profiles[student_profile_id].update(data.model_dump(exclude_none=True))
        return StudentProfileResponse(**_student_profiles[student_profile_id])

    def delete(self, student_profile_id: UUID):
        _student_profiles[student_profile_id]["is_active"] = False
        return StudentProfileResponse(**_student_profiles[student_profile_id])


student_profile_service = StudentProfileService()