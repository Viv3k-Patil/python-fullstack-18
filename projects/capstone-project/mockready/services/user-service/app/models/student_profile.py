from sqlalchemy import Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date

class StudentProfile(Base):
    __tablename__ = "student_profile"

    student_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    batch_id: Mapped[int] = mapped_column(Integer, ForeignKey("batch.batch_id"), nullable=False)
    enrollment_number: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    skills: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)