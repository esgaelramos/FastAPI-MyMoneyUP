from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean

from . import Users
from . import Roles
from . import Endpoints
from . import GroupsRoles
from . import UsersGroups
from . import EndpointsGroups
from core.bases.BaseModels import BaseModel


class Groups(BaseModel):
    __tablename__ = "groups"

    group_name: Mapped[str] = mapped_column(String(75), index=True, nullable=False, unique=True)
    group_description: Mapped[str] = mapped_column(String(255), index=True, nullable=True)
    group_status: Mapped[bool] = mapped_column(Boolean, default=False)

    # relationship
    roles: Mapped[List["Roles.Roles"]] = relationship(secondary=GroupsRoles, back_populates="back_groups_roles", lazy="selectin")

    # back_populates
    back_users_groups: Mapped["Users.Users"] = relationship(secondary=UsersGroups.users_groups, back_populates="groups")
    back_endpoints_groups: Mapped["Endpoints.Endpoints"] = relationship(secondary=EndpointsGroups.endpoints_groups, back_populates="groups")

    def __repr__(self) -> str:
        return self.group_name
