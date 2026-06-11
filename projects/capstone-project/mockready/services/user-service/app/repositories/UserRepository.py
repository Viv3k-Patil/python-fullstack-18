
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: UserCreate) -> User:
        user_data = data.model_dump()
        user_data["hashed_password"] = user_data.pop("password")
        user = User(**user_data)
        self.db.add(user)

        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(
            select(User).where(
                User.user_id == user_id,
                User.is_active == True
            )
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email.ilike(email))
        )
        return result.scalar_one_or_none()

    async def soft_delete(self, user_id: int) -> bool:
        result = await self.db.execute(
            select(User).where(User.user_id == user_id)
        )

        user = result.scalar_one_or_none()

        if not user:
            return False

        user.is_active = False

        await self.db.flush()

        return True

    async def update(
        self,
        user: User,
        data: UserUpdate
    ) -> User:

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)

        await self.db.flush()
        await self.db.refresh(user)

        return user

    async def get_all(
        self,
        page: int,
        size: int
    ) -> tuple[list[User], int]:

        result = await self.db.execute(
            select(User)
            .where(User.is_active == True)
            .offset((page - 1) * size)
            .limit(size)
        )

        users = result.scalars().all()

        count_result = await self.db.execute(
            select(User).where(User.is_active == True)
        )

        total = len(count_result.scalars().all())

        return users, total