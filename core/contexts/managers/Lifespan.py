"""
    Módulo que define el contexto asincrónico 'lifespan' para el manejo 
    del ciclo de vida de una aplicación FastAPI.

    Este módulo utiliza FastAPI y SQLAlchemy para gestionar el ciclo de 
    vida de la aplicación, creando tablas en la base de datos si existen 
    y cerrando la conexión a la base de datos al finalizar la aplicación.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from settings import SETTINGS
from core.databases.configs.ConfigPostgreSQL import CONNECTION_DATABASE



@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    """
        Contexto asincrónico para el manejo del ciclo de vida de una aplicación FastAPI.

        Args:
            app (FastAPI): Instancia de la aplicación FastAPI.

        Yields:
            None
    """
    
    if SETTINGS.EXISTS_TABLES:
        await CONNECTION_DATABASE.create_all()

    yield

    await CONNECTION_DATABASE.close()
