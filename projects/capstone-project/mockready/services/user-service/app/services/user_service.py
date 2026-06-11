"""
services/user_service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from app.schemas.user import UserCreate, UserResponse,UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.UserRepository import UserRepository
from app.core.exceptions import NotFoundException

class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def create(self, data: UserCreate) -> UserResponse:
        user = await self.user_repo.create(data)
        return UserResponse.model_validate(user)
    
    async def get_by_id(self, user_id: int) -> UserResponse:
        user = await self.user_repo.get_by_id(user_id)
        return UserResponse.model_validate(user)
    
    async def get_all(self, page: int, size: int) -> tuple[list[UserResponse], int]:
        users, total = await self.user_repo.get_all(page, size)
        return [UserResponse.model_validate(u) for u in users], total
    
    async def update(self, user_id: int, data: UserUpdate) -> UserResponse:

        user = await self.user_repo.get_by_id(user_id)

        if not user:
            raise NotFoundException("User not found")

        updated_user = await self.user_repo.update(
        user,
        data
    )

        return UserResponse.model_validate(updated_user)
    
    async def delete(self, user_id: int):
        return await self.user_repo.soft_delete(user_id)