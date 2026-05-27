

from app.schemas.booking_history import BookingHistoryCreate, BookingHistoryResponse, BookingHistoryUpdate
from app.repositories.booking_repository  import BookingRepository
from sqlalchemy.ext.asyncio import AsyncSession

class BookingHistoryService:

    def __init__(self, db: AsyncSession):
        self.booking_repo = BookingRepository(db)
    
    async def create(self, data: BookingHistoryCreate) -> BookingHistoryResponse:
        booking = await self.booking_repo.create(data)
        return BookingHistoryResponse.model_validate(booking)
    
    async def get_by_id(self, booking_history_id: int)-> BookingHistoryResponse:
        booking = await self.booking_repo.get_by_id(booking_history_id)
        return BookingHistoryResponse.model_validate(booking)
    
    async def get_all(self, page: int, size: int) -> tuple[list[BookingHistoryResponse], int]:
        bookings, total = await self.booking_repo.get_all(page, size)
        return [BookingHistoryResponse.model_validate(b) for b in bookings], total
    
    async def delete(self, booking_history_id: int):
        return await self.booking_repo.soft_delete(booking_history_id)