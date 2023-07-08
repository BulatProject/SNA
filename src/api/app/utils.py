from cryptography.fernet import Fernet

from src.core.settings import get_settings

settings = get_settings()


def encrypt_password(password: str) -> str:  # noqa
    sipher_suit = Fernet(bytes(settings.secret_key))  # noqa
    siphered_pass = sipher_suit.encrypt(bytes(password))  # noqa
    return str(siphered_pass)  # noqa
