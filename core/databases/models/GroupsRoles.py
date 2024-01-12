from sqlalchemy import ForeignKey, Table, Column

from core.bases.BaseModels import BaseModel


groups_roles = Table(
    "groups_roles",
    BaseModel.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("role_id", ForeignKey("roles.id")),
)
