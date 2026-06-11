"""
app/models/booking_history.py

SQLAlchemy model

Represents booking History table
inside PostgreSQL database.
"""
from sqlalchemy import (
    Integer,
    String,
    Boolean,
    Date
)
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import  date, datetime


class BookingHistory(Base):
    __tablename__ = "booking_history"

    booking_history_id : Mapped[int] = mapped_column(
        Integer,
        primary_key= True,
        autoincrement= True
    )

    booking_id : Mapped[int] = mapped_column(
       # ForeignKey("booking.booking_id"),
        Integer,
        nullable= False
    )

    trainer_id : Mapped[int] = mapped_column(
        #ForeignKey("trainer_profile.trainer_id"),
        Integer,
        nullable= False
    )
    action_data : Mapped[str] = mapped_column(
        String,
        nullable= False
    )
    reason : Mapped[str] = mapped_column(
        String,
        nullable= False
    )
    actioned_at : Mapped[date] = mapped_column(
        Date,
        nullable= True
    )

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)