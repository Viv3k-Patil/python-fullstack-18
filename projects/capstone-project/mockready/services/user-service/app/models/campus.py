from sqlalchemy import String, Integer, Boolean, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date


class Campus(Base):
    __tablename__ = "campus"

    campus_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(Text, nullable=False)
    cabin_count: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)