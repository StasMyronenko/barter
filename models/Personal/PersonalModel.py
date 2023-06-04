from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from models.Base import Base


class Personal(Base):
    __tablename__ = 'personal'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
