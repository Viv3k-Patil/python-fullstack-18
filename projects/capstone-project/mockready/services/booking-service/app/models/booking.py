"""
app/models/booking.py

SQLAlchemy model

Represents booking table
inside PostgreSQL database.
"""


from sqlalchemy import (
<<<<<<< HEAD
    Column,
=======
    Boolean,
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
    String,
    Integer,
    DateTime
)
<<<<<<< HEAD
from datetime import datetime , date
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


=======

from datetime import  date, datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from sqlalchemy import ForeignKey
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb

class Booking(Base):

    # Table name in database
    __tablename__ = "booking"

    booking_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

<<<<<<< HEAD

=======
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
    student_id : Mapped[int] = mapped_column(
       # ForeignKey("student_profile.student_id"),
        Integer,
        nullable=False

    )

    trainer_id : Mapped[int] = mapped_column(
        #ForeignKey("trainer_profile.trainer_id"),
        Integer,
        nullable=False
    )

<<<<<<< HEAD

=======
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
    cabin_id : Mapped[int] = mapped_column(
        #ForeignKey("cabin.cabin_id"),
        Integer,
        nullable=False
    )

    campus_id : Mapped[int] = mapped_column(
        #oreignKey("campus.campus_id"),
        Integer,
        nullable=False
    )

<<<<<<< HEAD
    campus_id = Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    interview_type = Mapped[str] = mapped_column(
=======
    interview_type : Mapped[str] = mapped_column(
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
        String,
        nullable=False
    )

<<<<<<< HEAD
    status = Mapped[str] = mapped_column(
=======
    status : Mapped[str] = mapped_column(
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
        String,
        nullable=False
    )

<<<<<<< HEAD

=======
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
    scheduled_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

<<<<<<< HEAD
    decline_count = Mapped[int] = mapped_column(
=======
    decline_count : Mapped[int] = mapped_column(
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
        Integer,
        default=0
    )

<<<<<<< HEAD
    created_at = Mapped[date] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
=======
    created_at : Mapped[date] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    #relationships
    # student_profile = relationship("StudentProfile", back_populates="bookings")
    # trainer_profile = relationship("TrainerProfile", back_populates="bookings")
    # cabin = relationship("Cabin", back_populates="bookings")
    # campus = relationship("Campus", back_populates="bookings")
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
