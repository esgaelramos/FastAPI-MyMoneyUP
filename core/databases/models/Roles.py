from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean

from . import Users
from . import Groups
from . import Endpoints
from core.bases.BaseModels import BaseModel


class Roles(BaseModel):
    __tablename__ = "roles"

    role_name: Mapped[str] = mapped_column(String(75), index=True, nullable=False, unique=True)
    role_description: Mapped[str] = mapped_column(String(255), index=True, nullable=True)
    role_status: Mapped[bool] = mapped_column(Boolean, default=False)

    # back_populates
    back_users_roles: Mapped["Users.Users"] = relationship(secondary=Users.users_roles, back_populates="roles")
    back_groups_roles: Mapped["Groups.Groups"] = relationship(secondary=Groups.groups_roles, back_populates="roles")
    back_endpoints_roles: Mapped["Endpoints.Endpoints"] = relationship(secondary=Endpoints.endpoints_roles, back_populates="roles")

    def __repr__(self) -> str:
        return self.role_name
