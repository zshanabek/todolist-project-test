from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.users import router as users_router
from app.db import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Mini User & Project Management API",
    lifespan=lifespan,
)

app.include_router(users_router)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
