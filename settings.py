from typing import List

from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """
        Configuracion global para las librerias principales y de terceros
        dentro del proyecto
    """

    # Configuracion de la aplicacion
    PROJECT_NAME: str = config("PROJECT_NAME", cast=str)
    URL_API_DOCUMENTATION: str = "/docs/"
    EXISTS_TABLES: bool = False

    # Configuracion del JWT
    ALGORITHM: str = config("ALGORITHM", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60  # Expira en 1 hora
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # Expira en 7 dias
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [] # Lista de URLs la cual podran acceder a la API
                                           # ["http://localhost:4400"]

    # Configuracion de la base de datos
    DATABASE_URL: str = config("DATABASE_URL", cast=str)

    # Configuracion del limitador de peticiones
    REQUESTS_PER_SECOND: int = 15 # Numero maximo de peticiones
    REQUEST_INTERVAL: int = 1 # Intervalo de tiempo por cada maximo de peticiones
    BLOCK_DURATION: int = 60 # Tiempo de bloqueo por exceder la cantidad de peticiones

    class Config:
        case_sensitive = True



SETTINGS = Settings()