"""
app/models/booking.py

SQLAlchemy model

Represents booking table
inside PostgreSQL database.
"""

from uuid import uuid4
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from datetime import datetime

from app.db.session import Base


class Booking(Base):

    # Table name in database
    __tablename__ = "booking"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    student_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    trainer_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    cabin_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    campus_id = Column(
        UUID(as_uuid=True),
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