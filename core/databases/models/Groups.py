from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean, ForeignKey, Table, Column

from . import Users
from . import Roles
from . import Endpoints
from core.bases.BaseModels import BaseModel


groups_roles = Table(
    "groups_roles",
    BaseModel.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("role_id", ForeignKey("roles.id")),
)


class Groups(BaseModel):
    __tablename__ = "groups"

    group_name: Mapped[str] = mapped_column(String(75), index=True, nullable=False, unique=True)
    group_description: Mapped[str] = mapped_column(String(255), index=True, nullable=True)
    group_status: Mapped[bool] = mapped_column(Boolean, default=False)

    # relationship
    roles: Mapped[List["Roles.Roles"]] = relationship(secondary=groups_roles, back_populates="back_groups_roles", lazy="selectin")

    # back_populates
    back_users_groups: Mapped["Users.Users"] = relationship(secondary=Users.users_groups, back_populates="groups")
    back_endpoints_groups: Mapped["Endpoints.Endpoints"] = relationship(secondary=Endpoints.endpoints_groups, back_populates="groups")

    def __repr__(self) -> str:
        return self.group_name
