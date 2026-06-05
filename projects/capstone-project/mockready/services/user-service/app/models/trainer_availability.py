from sqlalchemy import Integer, Boolean, Date, Time, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime


class TrainerAvailability(Base):
    __tablename__ = "trainer_availability"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    trainer_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    campus_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("campus.campus_id"),
        nullable=False
    )

    date: Mapped[Date] = mapped_column(
        Date,
        nullable=False
    )

    start_time: Mapped[Time] = mapped_column(
        Time,
        nullable=False
    )

    end_time: Mapped[Time] = mapped_column(
        Time,
        nullable=False
    )

    is_booked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # relationship with Campus
    campus: Mapped["Campus"] = relationship(
        "Campus",
        backref="trainer_availabilities"
    )