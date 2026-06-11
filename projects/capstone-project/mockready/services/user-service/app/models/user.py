from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime
from sqlalchemy import ForeignKey, func

class User(Base):
    __tablename__ = "users"


    user_id: Mapped[int] =mapped_column(
        Integer,
        primary_key= True,
        autoincrement=True
    )
    name: Mapped[str]= mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    campus_id: Mapped[int] = mapped_column(
        Integer,
        #ForeignKey("campus.campus_id"),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now()
    )
    #campus = relationship("User", back_populates="campus")
    