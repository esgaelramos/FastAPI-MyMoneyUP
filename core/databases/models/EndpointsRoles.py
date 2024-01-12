from sqlalchemy import ForeignKey, Table, Column

from core.bases.BaseModels import BaseModel


endpoints_roles = Table(
    "endpoints_roles",
    BaseModel.metadata,
    Column("endpoint_id", ForeignKey("endpoints.id")),
    Column("role_id", ForeignKey("roles.id")),
)
