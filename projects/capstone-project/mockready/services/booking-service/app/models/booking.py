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

from datetime import datetime

from app.db.session import Base


class Booking(Base):

    # Table name in database
    __tablename__ = "booking"

    booking_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = Column(
        Integer,
        nullable=False
    )

    trainer_id = Column(
        Integer,
        nullable=False
    )

    cabin_id = Column(
        Integer,
        nullable=False
    )

    campus_id = Column(
        Integer,
        nullable=False
    )

    interview_type = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    schedule_at = Column(
        DateTime,
        nullable=True
    )

    decline_count = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )