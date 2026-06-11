

from app.schemas.booking_history import BookingHistoryCreate, BookingHistoryResponse, BookingHistoryUpdate
from app.repositories.BookingHistoryRepository  import BookingHistoryRepository
from sqlalchemy.ext.asyncio import AsyncSession

class BookingHistoryService:

    def __init__(self, db: AsyncSession):
        self.booking_history_repo = BookingHistoryRepository(db)
    
    async def create(self, data: BookingHistoryCreate) -> BookingHistoryResponse:
        booking_history = await self.booking_history_repo.create(data)
        return BookingHistoryResponse.model_validate(booking_history)
    
    async def get_by_id(self, booking_history_id: int)-> BookingHistoryResponse:
        booking_history = await self.booking_history_repo.get_by_id(booking_history_id)
        return BookingHistoryResponse.model_validate(booking_history)
    
    async def get_all(self, page: int, size: int) -> tuple[list[BookingHistoryResponse], int]:
        bookings, total = await self.booking_history_repo.get_all(page, size)
        return [BookingHistoryResponse.model_validate(b) for b in bookings], total
    
    async def update(self,booking_history_id: int,data: BookingHistoryUpdate) -> BookingHistoryResponse:
        booking_history = await self.booking_history_repo.get_by_id(booking_history_id)
        if not booking_history:
            return None
        booking_history = await self.booking_history_repo.update(booking_history,data)
        return booking_history
    
    async def delete(self, booking_history_id: int):
        return await self.booking_history_repo.soft_delete(booking_history_id)
