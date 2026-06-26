from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("email", name="uq_users_email"),)

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(index=True, max_length=255)
