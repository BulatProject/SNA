from sqlalchemy import Column
from sqlalchemy import INTEGER
from sqlalchemy import String
from sqlalchemy.orm import relationship

from src.models import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = ({"comment": "User's accounts"},)

    user_id = Column(
        INTEGER, primary_key=True, nullable=False, comment="User's ID"
    )
    username = Column(
        String,
        comment="User's usermane",
    )
    password = Column(
        String,
        comment="User's password",
    )
    email = Column(
        String,
        unique=True,
        comment="User's email",
    )

    posts = relationship("Post", back_populates="user")
    likes = relationship("Likes", back_populates="user")
