from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.project import Project


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("email", name="uq_users_email"),)

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(index=True, max_length=255)
    projects: list["Project"] = Relationship(
        back_populates="owner",
        sa_relationship_kwargs={"cascade": "all, delete-orphan", "passive_deletes": True},
    )
