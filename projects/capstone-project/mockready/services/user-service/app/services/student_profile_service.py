from app.schemas.student_profile import StudentProfileResponse, StudentProfileCreate
from app.repositories.StudentProfileRepository import StudentProfileRepository
from sqlalchemy.ext.asyncio import AsyncSession

class StudentProfileService:

    def __init__(self, db: AsyncSession):
        self.student_profile_repo = StudentProfileRepository(db)
    
    async def create(self, data: StudentProfileCreate) -> StudentProfileResponse:
        student_profile = await self.student_profile_repo.create(data)
        return StudentProfileResponse.model_validate(student_profile)
    
    async def get_by_id(self, student_profile_id: int)-> StudentProfileResponse:
        student_profile = await self.student_profile_repo.get_by_id(student_profile_id)
        return StudentProfileResponse.model_validate(student_profile)
    
    async def get_all(self, page: int, size: int) -> tuple[list[StudentProfileResponse], int]:
        student_profiles, total = await self.student_profile_repo.get_all(page, size)
        return [StudentProfileResponse.model_validate(sp) for sp in student_profiles], total