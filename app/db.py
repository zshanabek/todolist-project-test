import os
from collections.abc import Generator

from sqlmodel import Session, create_engine

from app.models import User

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@db:5432/user_projects",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_db_and_tables() -> None:
    User.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
