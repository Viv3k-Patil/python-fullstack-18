"""
app/models/booking.py

SQLAlchemy model

Represents booking table
inside PostgreSQL database.
"""


from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)
from datetime import datetime , date
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base



class Booking(Base):

    # Table name in database
    __tablename__ = "booking"

    booking_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    student_id : Mapped[int] = mapped_column(
       # ForeignKey("student_profile.student_id"),
        Integer,
        nullable=False

    )

    trainer_id : Mapped[int] = mapped_column(
        #ForeignKey("trainer_profile.trainer_id"),
        Integer,
        nullable=False
    )


    cabin_id : Mapped[int] = mapped_column(
        #ForeignKey("cabin.cabin_id"),
        Integer,
        nullable=False
    )

    campus_id : Mapped[int] = mapped_column(
        #oreignKey("campus.campus_id"),
        Integer,
        nullable=False
    )

    campus_id = Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    interview_type = Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    status = Mapped[str] = mapped_column(
        String,
        nullable=False
    )


    scheduled_at : Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    decline_count = Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at = Mapped[date] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )