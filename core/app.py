from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core import core_router
from settings.config import settings


def get_middleware() -> list[Middleware]:
    return [
        Middleware(
            CORSMiddleware,
            allow_origins=settings.ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]


def create_app() -> FastAPI:
    app = FastAPI(title=settings.TITLE, openapi_url=settings.OPENAPI_URL, middleware=get_middleware())
    app.include_router(core_router.router)
    app.mount("/static", StaticFiles(directory=f"{settings.BASE_DIR}/static"), name="static")
    return app


app = create_app()
