from src.models.posts import Posts
from tests.factories.base_factory import AsyncSQLAlchemyFactory


class FirstPostFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Posts
