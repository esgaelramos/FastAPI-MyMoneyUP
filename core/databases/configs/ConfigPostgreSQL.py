"""
    Módulo que proporciona clases y funciones para trabajar con bases de 
    datos utilizando SQLAlchemy de manera asíncrona.

    Este módulo incluye la definición de la clase `Base`, que sirve como clase base para 
    las declaraciones SQLAlchemy, y la clase `AsyncDatabaseSession`, que proporciona una 
    interfaz para trabajar con sesiones de base de datos de manera asíncrona.

    Además, se define la instancia `CONNECTION_DATABASE` que representa una sesión de 
    base de datos asíncrona preconfigurada.
"""

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine,
)

from settings import SETTINGS


class Base(DeclarativeBase):
    """
    Clase base para las declaraciones SQLAlchemy.
    """

    pass


class AsyncDatabaseSession:
    """
    Clase que proporciona una interfaz para trabajar con sesiones de base de datos SQLAlchemy de manera asíncrona.

    Atributos:
        url (str): La URL de la base de datos a la que se conectará.
        engine (AsyncEngine): El motor SQLAlchemy para la base de datos.
        SessionLocal (sessionmaker): Generador de sesiones SQLAlchemy.
        session (AsyncSession): La sesión activa.
    """

    def __init__(self, url: str = SETTINGS.DATABASE_URL) -> None:
        """
        Inicializa una instancia de AsyncDatabaseSession.

        Args:
            url (str, opcional): La URL de la base de datos (predeterminado es la URL de configuración).
        """
        self.engine: AsyncEngine = create_async_engine(url, echo=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def create_all(self) -> None:
        """
        Crea todas las tablas definidas en el modelo
        en la base de datos.
        """
        async with self.engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    async def close(self) -> None:
        """
        Cierra la conexión con la base de datos.
        """
        await self.engine.dispose()

    async def __aenter__(self) -> AsyncSession:
        """
        Inicia una nueva sesión y la devuelve.

        Returns:
            AsyncSession: La sesión activa.
        """
        self.session: AsyncSession = self.SessionLocal()

        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Cierra la sesión cuando se utiliza en un
        contexto 'async with'.
        """
        await self.session.close()

    async def commit_rollback(self) -> None:
        """
        Intenta confirmar la transacción actual y,
        si falla, realiza un rollback.
        """
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise


CONNECTION_DATABASE = AsyncDatabaseSession()
