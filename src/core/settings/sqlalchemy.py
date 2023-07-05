from pydantic import AnyUrl

from src.core.settings.base import _BaseModel


class SqlAlchemySettings(_BaseModel):
    """SQLAlchemy settings"""

    url: AnyUrl | None = None
