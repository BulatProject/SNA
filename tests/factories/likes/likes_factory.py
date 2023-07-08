from src.models.likes import Likes
from tests.factories.base_factory import AsyncSQLAlchemyFactory


class FirstLikesFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Likes
