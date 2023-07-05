from pydantic import Field
from uvicorn.config import HTTPProtocolType
from uvicorn.config import LoopSetupType

from src.core.settings.base import _BaseModel


class UvicornSettings(_BaseModel):
    """Uvicorn Settings"""

    app: str = "main:app"
    host: str = "127.0.0.1"
    port: int = 8000
    loop: LoopSetupType = "auto"
    http: HTTPProtocolType = "auto"
    reload: bool = Field(default=None, description="Enable auto-reload.")
    workers: int | None = None
