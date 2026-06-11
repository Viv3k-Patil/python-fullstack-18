from sqlalchemy import String, Integer, Boolean, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import ForeignKey
from datetime import date

class TrainerCampus(Base):
    __tablename__ = "trainer_campus"

    trainer_campus_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    trainer_id: Mapped[int] = mapped_column(Integer, nullable=False)
    campus_id: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)