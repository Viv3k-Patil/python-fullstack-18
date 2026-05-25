

from io import DEFAULT_BUFFER_SIZE
from sqlalchemy.orm import Mapped, mapped_column

class Campus(Base):
    __tablename__ = "campus"
    
    campus_id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    ),
    name: Mapped[str]= mapped_column(
        String(200), nullable=False
    ),
    city: Mapped[str] = mapped_column(
        String(200), nullable=False
    ),
    address: Mapped[str] = mapped_column(
        Text, nullable=False
    ),
    cabin_count: Mapped[int]
    is_active: Mapped[bool]
    created_at: Mapped[date]
    

