from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import string,Column

class User (Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True
        )
    
    name: mapped[str]
    email: Mapped[str] = mapped_column(
        unique=True
        )
    