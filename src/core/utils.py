import logging
from typing import Union

import logging_json
from fastapi import FastAPI

from src.core import get_settings


settings = get_settings()


def protected_http_method(func):
    """Decorate your controller function with
    this decorator if requested user must
    be authorized.
    """
    func.__setattr__("protected", True)

    def inner(*args, **kwargs):
        return func(args, kwargs)

    return inner


def get_logger(level: Union[str, int]) -> logging.Logger:
    """
    Creates a JSON format Logger according to the Settings
    """
    middleware_logger = logging.getLogger(__name__)
    middleware_logger.setLevel(level)
    if not middleware_logger.handlers:
        st_formatter = logging_json.JSONFormatter()
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(st_formatter)
        middleware_logger.addHandler(stream_handler)
    return middleware_logger


def clear_app_routes(app: FastAPI):
    """
    Clear all app routes except built-in
    """
    for i, route in reversed(list(enumerate(app.routes))):
        if "service" in route.name:
            del app.routes[i]
