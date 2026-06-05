<<<<<<< HEAD

"""
services/booking_service.py

Business logic layer.

Responsibilities:
1. Database operations
2. Business rules
3. Data manipulation

NO HTTP logic here.
NO router logic here.
"""


from sqlalchemy import select
=======
from app.schemas.booking_schemas import BookingCreate, BookingResponse, BookingUpdate
from app.repositories.booking_repository  import BookingRepository
>>>>>>> 274b12e4 (User service file added)
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.booking import Booking
from app.schemas.booking_schemas import BookingCreate, BookingUpdate


class BookingService:

<<<<<<< HEAD
    @staticmethod
    async def create_booking(db: AsyncSession, payload: BookingCreate):
        booking = Booking(
            student_id=payload.student_id,
            trainer_id=payload.trainer_id,
            cabin_id=payload.cabin_id,
            campus_id=payload.campus_id,
            interview_type=payload.interview_type,
            status=payload.status
        )

        db.add(booking)
        await db.commit()
        await db.refresh(booking)

        return booking

    @staticmethod
    async def get_all_bookings(db: AsyncSession):
        result = await db.excute(
            select(Booking)
        )
        return result.scalars().all()

    @staticmethod
    async def get_booking_by_id(db: AsyncSession, booking_id: int):
        result = await db.execute(
            select(Booking).where(
                Booking.id == booking_id
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_booking(
        db: AsyncSession,
        booking_id: int,
        payload: BookingUpdate
    ):

        result = await db.execute(
            select(Booking).where(
                Booking.id == booking_id
            )
        )

        booking = result.scalar_one_or_none()

        if not booking:
            return None

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(booking, key, value)

        await db.commit()
        await db.refresh(booking)

        return booking

    @staticmethod
    async def delete_booking(
        db: AsyncSession,
        booking_id: int
    ):

        result = await db.execute(
            select(Booking).where(
                Booking.id == booking_id
            )
        )

        booking = result.scalar_one_or_none()

        if not booking:
            return None

        await db.delete(booking)

        await db.commit()

        return booking
=======
    def __init__(self, db: AsyncSession):
        self.booking_repo = BookingRepository(db)
    
    async def create(self, data: BookingCreate) -> BookingResponse:
        booking = await self.booking_repo.create(data)
        return BookingResponse.model_validate(booking)
    
    async def get_by_id(self, booking_id: int)-> BookingResponse:
        booking = await self.booking_repo.get_by_id(booking_id)
        return BookingResponse.model_validate(booking)
    
    async def get_all(self, page: int, size: int) -> tuple[list[BookingResponse], int]:
        bookings, total = await self.booking_repo.get_all(page, size)
        return [BookingResponse.model_validate(b) for b in bookings], total
    
    async def update(self,booking_id: int,data: BookingUpdate) -> BookingResponse:
        booking = await self.booking_repo.get_by_id(booking_id)
        if not booking:
            return None
        booking = await self.booking_repo.update(booking,data)

        return BookingResponse.model_validate(booking)




        

    async def delete(self, booking_id: int):
        return await self.booking_repo.soft_delete(booking_id)
    
>>>>>>> 274b12e4 (User service file added)
