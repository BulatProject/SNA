from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy_utc import utcnow


class TimingMixin:
    created_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        nullable=False,
        comment="When row was created",
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        onupdate=utcnow(),
        nullable=False,
        comment="Last time row was updated",
    )
