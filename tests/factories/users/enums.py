from enum import Enum

from src.api.app import utils


PAS_1 = utils.encrypt_password("pass_1")
PAS_2 = utils.encrypt_password("pass_2")
PAS_3 = utils.encrypt_password("pass_3")


USERNAME_1 = utils.encrypt_password("SomeRandomUsername_1")
USERNAME_2 = utils.encrypt_password("SomeRandomUsername_2")
USERNAME_3 = utils.encrypt_password("SomeRandomUsername_3")


EMAIL_1 = utils.encrypt_password("some_mail_1@gmail.com")
EMAIL_2 = utils.encrypt_password("some_mail_2@gmail.com")
EMAIL_3 = utils.encrypt_password("some_mail_3@gmail.com")


class FirstUser(Enum):
    USERNAME = USERNAME_1
    PASS = PAS_1
    EMAIL = EMAIL_1


class SecondUser(Enum):
    USERNAME = USERNAME_2
    PASS = PAS_2
    EMAIL = EMAIL_2


class ThirdUser(Enum):
    USERNAME = USERNAME_3
    PASS = PAS_3
    EMAIL = EMAIL_3
