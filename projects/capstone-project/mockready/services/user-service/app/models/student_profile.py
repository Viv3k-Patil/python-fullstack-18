from sqlalchemy import Integer, String, ForeignKey, Date, Boolean
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
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.user_id"), nullable=False)
    batch_id: Mapped[int] = mapped_column(Integer, ForeignKey("campus.campus_id"), nullable=False)
    skills: Mapped[str] = mapped_column(String(100), nullable=False)
    enrollment_number: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
