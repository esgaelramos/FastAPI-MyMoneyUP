from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Integer, ForeignKey


from . import Users
from core.bases.BaseModels import BaseModel


class HistoricalMovements(BaseModel):
    __tablename__ = "historical_movements"

    url_request: Mapped[str] = mapped_column(String(255), nullable=True)
    type_request: Mapped[str] = mapped_column(String(10), nullable=True)
    system: Mapped[str] = mapped_column(String(255), nullable=True)
    user_ip: Mapped[str] = mapped_column(String(255), nullable=True)
    user_browser: Mapped[str] = mapped_column(String, nullable=True)
    query: Mapped[str] = mapped_column(String, nullable=True)
    details: Mapped[str] = mapped_column(String, nullable=True)

    # relationship
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    user: Mapped["Users.Users"] = relationship(back_populates="back_historical_movements_users", lazy="selectin")

    def __repr__(self) -> str:
        return self.user.email
