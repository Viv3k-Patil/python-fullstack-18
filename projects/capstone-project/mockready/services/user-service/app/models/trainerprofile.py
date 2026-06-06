from sqlalchemy import String, Integer, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date


class TrainerProfile(Base):
    __tablename__ = "trainer_profile"

    trainer_profile_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.user_id"),
        nullable=False
    )

    skills: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    experience_years: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    rating: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    total_sessions: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )