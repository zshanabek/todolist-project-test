from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.user import User


class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=500)
    owner_id: int = Field(
        foreign_key="users.id",
        nullable=False,
        ondelete="CASCADE",
    )
    owner: Optional["User"] = Relationship(back_populates="projects")
