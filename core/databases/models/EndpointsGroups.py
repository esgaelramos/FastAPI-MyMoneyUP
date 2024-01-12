from sqlalchemy import ForeignKey, Table, Column

from core.bases.BaseModels import BaseModel


endpoints_groups = Table(
    "endpoints_groups",
    BaseModel.metadata,
    Column("endpoint_id", ForeignKey("endpoints.id")),
    Column("group_id", ForeignKey("groups.id")),
)
