from sqlalchemy import ForeignKey, Table, Column

from core.bases.BaseModels import BaseModel


users_groups = Table(
    "users_groups",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("group_id", ForeignKey("groups.id")),
)
