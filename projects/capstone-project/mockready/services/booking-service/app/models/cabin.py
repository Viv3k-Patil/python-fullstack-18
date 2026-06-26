from sqlalchemy import Boolean,String,Integer,Date
from sqlalchemy.orm import Mapped,mapped_column
from app.core.database import Base


class Cabin(Base):
    __tablename__ = "cabin"


    cabin_id : Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        autoincrement = True                    
        )
    
    campus_id : Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )


    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default = True
        )
    cabin_number : Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
