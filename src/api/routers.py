from fastapi.routing import APIRouter

from src.api.app.endpoints import routers as routers_app


routers = APIRouter()

routers.include_router(routers_app, tags=["App"])
