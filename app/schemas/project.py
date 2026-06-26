from sqlmodel import Field, SQLModel


class ProjectCreate(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    owner_id: int


class ProjectRead(SQLModel):
    id: int
    name: str
    description: str | None
    owner_id: int
