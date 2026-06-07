from datetime import date
from sqlalchemy import String, Integer, Text, Date, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.core.database import Base



class TrainerProfile(Base):
    __tablename__ = "trainer_profile"

    trainer_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    experience_years: Mapped[int] = mapped_column(Integer, nullable=False)
    skills: Mapped[str] = mapped_column(Text, nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    total_sessions: Mapped[int] = mapped_column(Integer, nullable=True)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)