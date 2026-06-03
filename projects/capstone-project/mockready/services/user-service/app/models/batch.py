from sqlalchemy import String,Integer,Boolean,Date,func
from sqlalchemy.orm import Mapped,mapped_column
from app.core.database import Base
from datetime import date

class Batch(Base):
    
    __tablename__="batch"
    
    batch_id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
        )
    campus_id:Mapped[int]   = mapped_column(Integer,nullable=False)
    name: Mapped[str]       = mapped_column(String(100),nullable=False)
    course:Mapped[str]      = mapped_column(String(100),nullable=False)
    start_date:Mapped[date] =mapped_column(Date,default=func.current_date(),nullable=False)  
    end_date:Mapped[date]   =mapped_column(Date,nullable=False)
    is_active: Mapped[bool] =mapped_column(Boolean,default=True,nullable=False)