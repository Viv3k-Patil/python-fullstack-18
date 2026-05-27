from app.schemas.booking_schemas import BookingCreate, BookingResponse
from app.repositories.booking_repository  import BookingRepository
from sqlalchemy.ext.asyncio import AsyncSession

class BookingService:

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
    
    async def delete(self, booking_id: int):
        return await self.booking_repo.soft_delete(booking_id)
    
