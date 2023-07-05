from fastapi.routing import APIRouter

from src.core.utils import protected_http_method


routers = APIRouter()


@protected_http_method
@routers.post("/registration")
async def registration():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/login")
async def login():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/logout")
async def logout():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/new-post")
async def post_new_post():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.get("/post/{post_number}")
async def get_post():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.patch("/post/{post_number}")
async def patch_post():
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.delete("/post/{post_number}")
async def delete_post():
    return {"Message": "This page is under developement"}
