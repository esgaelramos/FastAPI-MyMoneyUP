"""
    Módulo que define las clases ResponseEntities y PaginationEntities para manejar 
    respuestas y paginación.

    Este módulo utiliza Pydantic y typing para definir modelos de respuesta y 
    paginación genéricos.
"""

from typing import Generic, TypeVar, Optional, List

from pydantic import BaseModel


T = TypeVar("T")


class ResponseEntities(BaseModel):
    """
    Clase para manejar respuestas con un status, detalle y un resultado opcional.

    Atributos:
        status (int, opcional): El código de estado de la respuesta.
        detail (str, opcional): Detalle de la respuesta.
        result (T, opcional): El resultado de la respuesta, que puede ser de cualquier tipo genérico T.
    """

    status: Optional[int]
    detail: Optional[str]
    result: Optional[T] = None


class PaginationEntities(BaseModel, Generic[T]):
    """
    Clase para manejar paginación de resultados.

    Atributos:
        page_number (int): Número de página actual.
        page_size (int): Tamaño de la página.
        total_pages (int): Número total de páginas.
        total_record (int): Número total de registros.
        content (List[T]): Lista de elementos de tipo T en la página actual.
    """

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[T]
