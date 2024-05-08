from fastapi import APIRouter
from fastapi.responses import FileResponse

from settings.config import settings

router = APIRouter()


@router.get("/healthcheck", status_code=200, tags=["healthcheck"])
async def healthcheck() -> dict[str, str]:
    return {"detail": "OK"}


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    fav_path = f"{settings.BASE_DIR}/static/favicon.ico"
    return FileResponse(fav_path)
