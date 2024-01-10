from fastapi import FastAPI

from .authentication.routers import authentication_routers
from .administration.routers import administration_routers
from .management.routers import management_routers


def all_routers(app: FastAPI) -> None:
    authentication_routers(app=app)
    administration_routers(app=app)
    management_routers(app=app)
