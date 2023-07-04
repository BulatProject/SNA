from fastapi.routing import APIRouter


routers = APIRouter()


@routers.post("/registration")
async def registration():
    return {"Message": "This page is under developement"}


@routers.post("/login")
async def login():
    return {"Message": "This page is under developement"}


@routers.post("/logout")
async def logout():
    return {"Message": "This page is under developement"}


@routers.post("/new-post")
async def post_new_post():
    return {"Message": "This page is under developement"}


@routers.get("/post/{post_number}")
async def get_post():
    return {"Message": "This page is under developement"}


@routers.patch("/post/{post_number}")
async def patch_post():
    return {"Message": "This page is under developement"}


@routers.delete("/post/{post_number}")
async def delete_post():
    return {"Message": "This page is under developement"}
