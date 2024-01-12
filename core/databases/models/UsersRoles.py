from sqlalchemy import ForeignKey, Table, Column

from core.bases.BaseModels import BaseModel


users_roles = Table(
    "users_roles",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id")),
)
