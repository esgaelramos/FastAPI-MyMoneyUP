"""
    Este archivo centraliza todas las configuraciones iniciales del proyecto FastAPI. Aquí se pueden realizar 
    ajustes y agregar middlewares necesarios para el proyecto.

    Contenido del Archivo:
    - Configuración del Proyecto FastAPI
        - `title`: Define el nombre del proyecto como se mostrará en la documentación.
        - `openapi_url`: Especifica la ruta para acceder al archivo JSON OpenAPI, utilizado para la documentación automática.
        - ...

    - Middlewares
        - `CORSMiddleware`: Permite configurar y controlar las políticas CORS (Cross-Origin Resource Sharing) para gestionar 
        el acceso a la API desde diferentes dominios.
            - `allow_origins`: Define los orígenes permitidos para las solicitudes CORS.
            - `allow_credentials`: Habilita el intercambio de credenciales, permitiendo el envío de cookies y encabezados de autenticación.
            - `allow_methods`: Especifica los métodos HTTP permitidos para las solicitudes CORS (p. ej., "GET", "POST", "*").
            - `allow_headers`: Define los encabezados permitidos en las solicitudes CORS.
            - ...
    ...

    - Inicialización de Routers
        - La función `all_routers` inicializa todos los routers definidos en el módulo `core.routers.routers` y 
        los agrega a la instancia de FastAPI (`app`).

    - Ruta de Redirección a la Documentación: `/docs`
        - Realiza una redirección a la documentación interactiva generada automáticamente por FastAPI.
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from settings import SETTINGS
from core.routers.routers import all_routers



# Crea una instancia de FastAPI
app = FastAPI(
    title=SETTINGS.PROJECT_NAME,                                # Nombre del proyecto
    openapi_url=f"{SETTINGS.URL_API_DOCUMENTATION}openapi.json" # Ruta para la documentacion
)


# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Inicializara todos los routers
all_routers(app=app)


# Redireccion a la ruta de la documentacion
@app.get("/", include_in_schema=False)
async def documentation() -> RedirectResponse:
    """
        Ruta de redirección a la documentación principal.
        Esta función redirige a la ruta `/documentation` utilizando `RedirectResponse`.

        Returns:
            RedirectResponse: Redirección a la ruta `/documentation`.
    """
    return RedirectResponse(url="/docs")