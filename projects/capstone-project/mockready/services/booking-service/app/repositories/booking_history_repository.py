from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.booking_history import BookingHistoryCreate, BookingHistoryUpdate
from app.models.booking_history import BookingHistory
from sqlalchemy import select

class BookingHistoryRepository:
    def __init__(self , db: AsyncSession):
        self.db = db

    async def create(self,data : BookingHistoryCreate) -> BookingHistory:
        # BookingHistoryCreate -> type -> pydantic schmema
        # BookingHistory -> type > sqlalchemy model

        # step 1: send data to db
        # data-> model, schema -> model and then send it to db
        # 1. model_dump -> pydantic object-> python dict
        # 2. dict unpack

        booking_history = BookingHistory(**data.model_dump())
        self.db.add(booking_history)
        await self.db.flush()
        await self.db.refresh(booking_history)
        return booking_history
    
    async def get_by_id(self,booking_history_id : int) -> BookingHistory | None:
        result = await self.db.execute(
         select(BookingHistory).where(BookingHistory.booking_history_id == booking_history_id, BookingHistory.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def soft_delete(self, booking_history_id : int) -> bool:
        result = await self.db.execute(
            select(BookingHistory.where(BookingHistory.booking_history_id == booking_history_id))
        )
        booking_history = result.scalar_one_or_none()
        if not booking_history:
            return False
        booking_history.is_active == False
        await self.db.flush()
        return True
    
    async def get_all(self, page: int, size: int) -> tuple[list[BookingHistory], int]:
        result = await self.db.execute(
            select(BookingHistory).where(BookingHistory.is_active == True).offset((page-1)*size).limit(size)
        )
        bookings_history = result.scalars().all()

        count_result = await self.db.execute(
            select(BookingHistory).where(BookingHistory.is_active == True)
        )
        total = len(count_result.scalars().all())
        return bookings_history , total

    