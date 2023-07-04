from fastapi import FastAPI

from src.api import routers


app = FastAPI()

app.include_router(routers)
