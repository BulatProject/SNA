from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy import Text
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.models.base_class import Base
from src.models.mixins import TimingMixin


class Posts(TimingMixin, Base):
    __tablename__ = "posts"
    __table_args__ = ({"comment": "Posts by users"},)

    like_id = Column(
        INTEGER,
        primary_key=True,
        nullable=False,
        comment="Post's ID",
    )
    user_id = mapped_column(
        ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False,
        comment="Post's owner",
    )
    text = Column(
        Text,
        nullable=False,
        comment="Post's content",
    )

    user = relationship("User", back_populates="posts")
    likes = relationship("Likes", back_populates="posts")
