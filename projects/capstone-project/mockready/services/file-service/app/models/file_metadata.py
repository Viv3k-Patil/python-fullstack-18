# from sqlalchemy import String,Integer,Date
# from sqlalchemy.orm import Mapped,mapped_column
# from app.core.database import Base
# from datetime import date

# class FileMetadata(Base):
    
#     __tablename__="file_metadata"
    
#     id:Mapped[int] = mapped_column(
#         Integer,
#         primary_key=True,
#         autoincrement=True
#     )
    
#     student_id: Mapped[int] = mapped_column(Integer, nullable=False)
#     student_name: Mapped[str] = mapped_column(String(100), nullable=False)

#     stored_path: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
#     file_type: Mapped[str] = mapped_column(String(100), nullable=False)
#     size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
#     uploaded_at: Mapped[date] = mapped_column(Date, nullable=False)

# app/models/file_metadata.py

from sqlalchemy import String, Integer, Date,Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id:           Mapped[int]  = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id:   Mapped[int]  = mapped_column(Integer, nullable=False)
    student_name: Mapped[str]  = mapped_column(String(100), nullable=False)
    stored_path:  Mapped[str]  = mapped_column(String(100), nullable=False)
    file_type:    Mapped[str]  = mapped_column(String(100), nullable=False)
    size_bytes:   Mapped[int]  = mapped_column(Integer, nullable=False)
    uploaded_at:  Mapped[date] = mapped_column(Date, nullable=True)   
    is_active:    Mapped[bool] = mapped_column(Boolean,nullable=False)  