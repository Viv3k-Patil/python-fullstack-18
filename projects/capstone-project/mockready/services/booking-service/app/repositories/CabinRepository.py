from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models.cabin import Cabin
from datetime import datetime
class CabinRepository:
   def __init__(self,db:AsyncSession):
        self.db = db

async def get_available_cabins(self, start_time: datetime, end_time: datetime) -> list[Cabin]:
    exiting_bookings = (select(Booking.id)
        .where(
            Booking.cabin_id == Cabin.cabin_id,
            Booking.start_time < start_time,
            Booking.end_time > end_time
        )
    )



     select(Cabin).where(
        Cabin.is_active == True,
        not_exists( exiting_bookings


        ).order_by(Cabin.cabin_number)
    )

    

  
        