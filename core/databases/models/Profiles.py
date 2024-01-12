from datetime import date

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Integer, ForeignKey, Date

from . import Users
from core.bases.BaseModels import BaseModel


class Profiles(BaseModel):
    __tablename__ = "profiles"

    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    document: Mapped[str] = mapped_column(String(50), index=True, nullable=False, unique=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)

    # relationship
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=True)
    user: Mapped["Users.Users"] = relationship(overlaps="profile")

    def __repr__(self) -> str:
        return self.document
