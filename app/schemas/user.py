from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserCreate(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr


class UserRead(SQLModel):
    id: int
    name: str
    email: EmailStr
