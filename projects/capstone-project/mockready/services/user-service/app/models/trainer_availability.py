from sqlalchemy import String, Integer, Boolean, Date,DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import ForeignKey
from datetime import date,datetime

class TrainerAvailability(Base):
    __tablename__ = "trainer_availability"

    trainer_availability_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    trainer_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainer_profile.trainer_id"), nullable=False)
    campus_id: Mapped[int] = mapped_column(Integer, ForeignKey("campus.campus_id"), nullable=False)
    start_time: Mapped[datetime] =mapped_column(DateTime(timezone=True), nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    #is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)