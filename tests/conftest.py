"""This package implements a set of unit tests
using the postgreSQL database as storage.
running command:
`python -m pytest tests --asyncio-mode=auto`

To update the snapshots run tests with command:
`python -m pytest tests --asyncio-mode=auto --snapshot-update`
"""
import asyncio
import os.path
from asyncio import current_task
from typing import Generator

import nest_asyncio
import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from src.core.database import get_session
from src.core.settings import settings as project_settings
from src.main import get_application
from src.models.base_class import Base


nest_asyncio.apply()


pg_dms_url = os.path.split(project_settings.postgres.url)[0]
sqlalchemy_domain_url = os.path.split(project_settings.sqlalchemy.url)[0]


SQLALCHEMY_DATABASE_URL = f"{pg_dms_url}/test"
ALEMBIC_DATABASE_URL = f"{sqlalchemy_domain_url}/test"


test_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL + "?prepared_statement_cache_size=0",
)

testing_session_local = async_sessionmaker(
    bind=test_engine, autocommit=False, autoflush=False, expire_on_commit=False
)

factory_session = async_scoped_session(
    testing_session_local, scopefunc=current_task
)


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def creating_db():
    """This fixture creates new database `test` using the same
    database managment system as the main application.
    """
    db_engine = create_engine(f"{sqlalchemy_domain_url}")
    with db_engine.connect() as conn:
        conn.execute(text("COMMIT"))
        try:
            conn.execute(text("CREATE DATABASE test"))
        except ProgrammingError:
            conn.execute(text("DROP DATABASE IF EXISTS test WITH (FORCE)"))
            conn.execute(text("CREATE DATABASE test"))
    yield
    with db_engine.connect() as conn:
        conn.execute(text("COMMIT"))
        conn.execute(text("DROP DATABASE IF EXISTS test WITH (FORCE)"))


@pytest.fixture(scope="session")
def engine() -> AsyncEngine:
    yield test_engine


@pytest_asyncio.fixture(scope="function")
async def db_conn(engine: AsyncEngine) -> AsyncConnection:
    async with engine.connect() as connection:
        await connection.run_sync(Base.metadata.create_all)
        await connection.commit()
        yield connection


async def get_db_session():
    async with testing_session_local() as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def async_client():
    test_app: FastAPI = get_application()
    test_app.dependency_overrides[get_session] = get_db_session
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        yield ac
