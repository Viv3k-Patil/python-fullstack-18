"""
app/models/booking.py

SQLAlchemy model

Represents booking table
inside PostgreSQL database.
"""


from sqlalchemy import (
    Boolean,
    String,
    Integer,
    DateTime
)

from datetime import  date, datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from sqlalchemy import ForeignKey

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

    interview_type : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    status : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    scheduled_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    decline_count : Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at : Mapped[date] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    #relationships
    # student_profile = relationship("StudentProfile", back_populates="bookings")
    # trainer_profile = relationship("TrainerProfile", back_populates="bookings")
    # cabin = relationship("Cabin", back_populates="bookings")
    # campus = relationship("Campus", back_populates="bookings")