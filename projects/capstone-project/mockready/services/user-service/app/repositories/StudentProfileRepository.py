from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.student_profile import StudentProfileCreate,StudentProfileUpdate   
from app.models.student_profile import StudentProfile


class StudentProfileRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create(self, data: StudentProfileCreate) -> StudentProfile:
        student_profile = StudentProfile(**data.model_dump())
        self.db.add(student_profile)
        await self.db.flush()
        await self.db.refresh(student_profile)
        return student_profile

    async def get_by_id(self, student_profile_id: int) -> StudentProfile | None:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.student_id == student_profile_id, StudentProfile.is_active == True)
        )
        return result.scalar_one_or_none()

    async def get_all(self, page: int, size: int) -> tuple[list[StudentProfile], int]:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.is_active == True).offset((page - 1) * size).limit(size)
        )
        student_profiles = result.scalars().all()

        count_result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.is_active == True)
        )
        total = len(count_result.scalars().all())
        return student_profiles, total

    async def update(self, student_profile: StudentProfile, data: StudentProfileUpdate) -> StudentProfile:
        for key, value in data.model_dump().items():
            setattr(student_profile, key, value)
        await self.db.flush()
        await self.db.refresh(student_profile)
        return student_profile

    async def soft_delete(self, student_profile_id: int) -> bool:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.student_id == student_profile_id)
        )
        student_profile = result.scalar_one_or_none()
        if not student_profile:
            return False
        student_profile.is_active = False
        await self.db.flush()
        return True

    async def get_by_id(self, student_profile_id: int) -> StudentProfile | None:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.student_id == student_profile_id, StudentProfile.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def get_all(self,page:int , size : int)->tuple[list[StudentProfile],int]:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.is_active==True).offset((page-1)*size).limit(size)
        )
        student_profiles= result.scalars().all()

        count_result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.is_active == True)
        )
        total = len(count_result.scalars().all())
        return student_profiles,total

    async def update(self, student_profile: StudentProfile, data: StudentProfileUpdate) -> StudentProfile:
        for key, value in data.model_dump().items():
            setattr(student_profile, key, value)
        await self.db.flush()
        await self.db.refresh(student_profile)
        return student_profile

    async def soft_delete(self, student_profile_id : int) -> bool:
        result = await self.db.execute(
            select(StudentProfile).where(StudentProfile.student_id == student_profile_id)
 )
        student_profile = result.scalar_one_or_none()
        if not student_profile:
            return False
        student_profile.is_active = False
        await self.db.flush()
        return True