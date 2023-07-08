from enums import FirstUser
from enums import SecondUser
from enums import ThirdUser

from src.models.users import User
from tests.factories.base_factory import AsyncSQLAlchemyFactory


class FirstUserFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = User

    user_id = 1
    username = FirstUser.USERNAME.value
    password = FirstUser.PASS.value
    email = FirstUser.EMAIL.value


class SecondUserFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = User

    user_id = 2
    username = SecondUser.USERNAME.value
    password = SecondUser.PASS.value
    email = SecondUser.EMAIL.value


class ThirdtUserFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = User

    user_id = 3
    username = ThirdUser.USERNAME.value
    password = ThirdUser.PASS.value
    email = ThirdUser.EMAIL.value
