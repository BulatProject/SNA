from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_session
from src.core.utils import protected_http_method


routers = APIRouter()


@protected_http_method
@routers.post("/registration")
async def registration(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/login")
async def login(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/logout")
async def logout(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.post("/new-post")
async def post_new_post(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.get("/post/{post_number}")
async def get_post(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.patch("/post/{post_number}")
async def patch_post(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}


@protected_http_method
@routers.delete("/post/{post_number}")
async def delete_post(
    session: AsyncSession = Depends(get_session),
):
    return {"Message": "This page is under developement"}
