from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy import String, Boolean, JSON, Table, Column, ForeignKey

from . import Roles
from . import Groups
from core.bases.BaseModels import BaseModel


endpoints_roles = Table(
    "endpoints_roles",
    BaseModel.metadata,
    Column("endpoint_id", ForeignKey("endpoints.id")),
    Column("role_id", ForeignKey("roles.id")),
)


endpoints_groups = Table(
    "endpoints_groups",
    BaseModel.metadata,
    Column("endpoint_id", ForeignKey("endpoints.id")),
    Column("group_id", ForeignKey("groups.id")),
)


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
    roles: Mapped[List["Roles.Roles"]] = relationship(secondary=endpoints_roles, back_populates="back_endpoints_roles", lazy="selectin")
    groups: Mapped[List["Groups.Groups"]] = relationship(secondary=endpoints_groups, back_populates="back_endpoints_groups", lazy="selectin")

    def __repr__(self) -> str:
        return self.endpoint_name
