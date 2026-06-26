from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.booking import BookingCreate, BookingUpdate
from app.models.booking import Booking



# booking repository

class BookingRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: BookingCreate) -> Booking:
        # BookingCreate -> type -> pydantic schmema
        # Booking -> type > sqlalchemy model

        # step 1: send data to db
        # data-> model, schema -> model and then send it to db
        # 1. model_dump -> pydantic object-> python dict
        # 2. dict unpack
        booking = Booking(**data.model_dump())
        self.db.add(booking)
        await self.db.flush()
        await self.db.refresh(booking)
        return booking
    
    async def get_by_id(self, booking_id: int) -> Booking | None:
        result = await self.db.execute(
            # this is statement
            select(Booking).where(Booking.booking_id ==booking_id, Booking.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Booking | None:
        result = await self.db.execute(select(Booking).where(Booking.name.ilike(name)))
        return result.scalar_one_or_none()
    
    async def soft_delete(self, booking_id: int) -> bool:
        result = await self.db.execute(
            select(Booking).where(Booking.booking_id == booking_id)
        )
        booking = result.scalar_one_or_none()
        if not booking:
            return False
        booking.is_active = False
        await self.db.flush()
        return True
    
    async def update(self, booking: Booking, data: BookingUpdate) -> Booking:
        for key, value in data.model_dump().items():
            # booking[key] = value
            setattr(booking, key, value)
        await self.db.flush()
        await self.db.refresh(booking)
        return booking
        
    async def get_all(self, page: int, size: int) -> tuple[list[Booking], int]:
        result = await self.db.execute(
            select(Booking).where(Booking.is_active == True).offset((page-1)*size).limit(size)
        )
        bookings = result.scalars().all()

        count_result = await self.db.execute(
            select(Booking).where(Booking.is_active == True)
        )
        total = len(count_result.scalars().all())

        return bookings , total


    async def get_all_available_cabins(self,start_time:datetime, end_time:datetime, ) ->list[Cabin]:
        result = await self.db.execute(
            select(Booking).where(
                Booking.is_active == True,
                Booking.start_time >= start_time,
                Booking.end_time <= end_time
            ).offset((page-1)*size).limit(size)
        )
        bookings = result.scalars().all()

        count_result = await self.db.execute(
            select(Booking).where(
                Booking.is_active == True,
                Booking.start_time >= start_time,
                Booking.end_time <= end_time
            )
        )
        total = len(count_result.scalars().all())

        return bookings , total