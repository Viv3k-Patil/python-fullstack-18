from app.schemas.booking import BookingCreate, BookingResponse, BookingUpdate
from app.repositories.BookingRepository import BookingRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.locks import booking_lock

class BookingService:

    def __init__(self, db, redis):
        self.repo = BookingRepository(db)
        self.redis = redis

    async def create_booking(self, data):

        # unique resource (VERY IMPORTANT)
        resource_id = f"{data.cabin_id}:{data.date}:{data.start_time}"

        async with booking_lock(self.redis, resource_id):

            # # 🔥 CRITICAL SECTION
            # cabin = await self.check_cabin_available(data)

            # if not cabin:
            #     raise Exception("Cabin not available")

            booking = await self.repo.create(data)

            return booking

    
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