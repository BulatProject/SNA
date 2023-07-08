from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.models.base_class import Base
from src.models.mixins import TimingMixin


class Likes(TimingMixin, Base):
    __tablename__ = "likes"
    __table_args__ = ({"comment": "Likes on posts by users"},)

    like_id = Column(
        INTEGER,
        primary_key=True,
        nullable=False,
        comment="Likes's ID",
    )
    user_id = mapped_column(
        ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False,
        comment="Like's owner",
    )
    post_id = mapped_column(
        ForeignKey("post.post_id", ondelete="CASCADE"),
        nullable=False,
        comment="Liked post",
    )

    user = relationship("User", back_populates="likes")
    post = relationship("Posts", back_populates="likes")
