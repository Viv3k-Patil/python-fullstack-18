from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.booking_schemas import (BookingCreate,BookingUpdate)

from app.models.booking import Booking

# booking repository

class BookingRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: BookingCreate) -> Booking:

        # BookingCreate -> Pydantic schema
        # Booking -> SQLAlchemy model
        # schema -> model -> db

        booking = Booking(**data.model_dump())

        self.db.add(booking)
        await self.db.flush()
        await self.db.refresh(booking)
        return booking

    async def get_by_id(self, booking_id: int) -> Booking | None:

        result = await self.db.execute(select(Booking).where(Booking.booking_id == booking_id,Booking.is_active == True))

        return result.scalar_one_or_none()

    async def get_all(self) -> list[Booking]:

        result = await self.db.execute(select(Booking).where(Booking.is_active == True)
        )

        return list(result.scalars().all())

    async def get_by_student_and_slot(
        self,
        student_id: int,
        slot_time
    ) -> Booking | None:

        result = await self.db.execute(

            select(Booking).where(
                Booking.student_id == student_id,
                Booking.slot_time == slot_time,
                Booking.is_active == True
            )
        )

        return result.scalar_one_or_none()

    async def soft_delete(
        self,
        booking: Booking
    ) -> bool:

        booking.is_active = False

        await self.db.flush()

        return not booking.is_active

    async def update(
        self,
        booking: Booking,
        data: BookingUpdate
    ) -> Booking:

        # update only provided fields
        updates = data.model_dump(exclude_none=True)

        for key, value in updates.items():

            setattr(booking, key, value)

        await self.db.flush()
        await self.db.refresh(booking)

        return booking