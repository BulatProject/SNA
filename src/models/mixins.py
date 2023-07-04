from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy_utc import utcnow


class TimingMixin:
    created_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        nullable=False,
        comment="Время создания записи",
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        onupdate=utcnow(),
        nullable=False,
        comment="Время последнего обновления записи",
    )
