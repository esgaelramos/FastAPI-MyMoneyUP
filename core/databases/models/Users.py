from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean, Table, Column, ForeignKey

from . import Roles
from . import Groups
from . import Profiles
from . import HistoricalMovements
from core.bases.BaseModels import BaseModel


users_roles = Table(
    "users_roles",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id")),
)


users_groups = Table(
    "users_groups",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("group_id", ForeignKey("groups.id")),
)


class Users(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), index=True, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(512), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    # relationship
    roles: Mapped[List["Roles.Roles"]] = relationship(secondary=users_roles, back_populates="back_users_roles", lazy="selectin")
    groups: Mapped[List["Groups.Groups"]] = relationship(secondary=users_groups, back_populates="back_users_groups", lazy="selectin")
    profile: Mapped["Profiles.Profiles"] = relationship(uselist=False, lazy="selectin")

    # back_populates
    back_historical_movements_users: Mapped["HistoricalMovements.HistoricalMovements"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return self.email
