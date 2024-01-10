"""
    Módulo que define la clase BaseModel, una clase base abstracta para los modelos de SQLAlchemy.

    Este módulo utiliza SQLAlchemy para definir modelos de base de datos con campos como id, 
    created_at y updated_at, que representan un identificador único, la fecha de creación y la
    fecha de última actualización de un registro, respectivamente.

    La clase BaseModel hereda de la clase Base proporcionada por la configuración de PostgreSQL 
    y establece la abstracción como True.
"""

from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from core.databases.configs.ConfigPostgreSQL import Base


class BaseModel(Base):
    """
    Clase base abstracta para modelos de SQLAlchemy.

    Attributes:
        id (Mapped[int]): Campo que representa un identificador único (clave primaria).
        created_at (Mapped[datetime]): Campo que representa la fecha de creación del registro.
        updated_at (Mapped[datetime]): Campo que representa la fecha de última actualización del registro.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
