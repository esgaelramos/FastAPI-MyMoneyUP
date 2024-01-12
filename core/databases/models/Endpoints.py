from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean, JSON

from . import Roles
from . import Groups
from . import EndpointsRoles
from . import EndpointsGroups
from core.bases.BaseModels import BaseModel


class Endpoints(BaseModel):
    __tablename__ = "endpoints"

    endpoint_name: Mapped[str] = mapped_column(String(255), index=True, nullable=True, unique=True)
    endpoint_url: Mapped[str] = mapped_column(String(512), index=True, nullable=False, unique=True)
    endpoint_request: Mapped[str] = mapped_column(String(10), nullable=False)
    endpoint_parameters: Mapped[str] = mapped_column(JSON, nullable=True)
    endpoint_description: Mapped[str] = mapped_column(String(512), index=True, nullable=True)
    endpoint_status: Mapped[bool] = mapped_column(Boolean, default=False)
    endpoint_authenticated: Mapped[bool] = mapped_column(Boolean, default=True)

    # relationship
    roles: Mapped[List["Roles.Roles"]] = relationship(
        secondary=EndpointsRoles.endpoints_roles, back_populates="back_endpoints_roles", lazy="selectin"
    )
    groups: Mapped[List["Groups.Groups"]] = relationship(
        secondary=EndpointsGroups.endpoints_groups, back_populates="back_endpoints_groups", lazy="selectin"
    )

    def __repr__(self) -> str:
        return self.endpoint_name
