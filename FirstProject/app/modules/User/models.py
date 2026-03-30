from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float
from database.db import Base

class User(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price:Mapped[float]=mapped_column(Float,nullable=False)
    quantity:Mapped[int]=mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    