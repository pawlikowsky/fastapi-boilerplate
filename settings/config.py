import os
import pathlib
from functools import lru_cache
from typing import List

from pydantic import Field


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict = {}
    TITLE: str = "FastAPI Project"
    OPENAPI_URL: str = "/openapi.json"


class DevelopmentConfig(BaseConfig):
    # Configure CORS
    ORIGINS: List[str] = [
        Field(
            default=[
                "http://localhost:8080",
                "http://0.0.0.0:8080",
            ]
        )
    ]


class ProductionConfig(BaseConfig):
    # Configure CORS
    ORIGINS: List[str] = [Field(default=["https://example.com"])]

    # DISABLE DOCS
    OPENAPI_URL: str = ""


class TestingConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
