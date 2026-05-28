from sqlalchemy import Boolean,String,Integer,Date
from sqlalchemy.orm import Mapped,mapped_column
from datetime import date
from app.core.database import Base

class Batch(Base):
  __tablename__ = "batch"


  batch_id: Mapped[int]= mapped_column(
      Integer,
    primary_key=True,
    autoincrement=True
)

  name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
  course:Mapped[str]= mapped_column(String(100),nullable=False,unique=True)
  start_date:Mapped[date]= mapped_column(Date,nullable=False)
  end_date:Mapped[date]= mapped_column(Date,nullable=False)
  is_active:Mapped[bool] = mapped_column(Boolean,default = True)
  #created_at:Mapped[date] = mapped_column(Date,nullable=False)
