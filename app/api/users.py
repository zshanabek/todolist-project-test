from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlmodel import Session

from app.db import get_session
from app.schemas.user import UserCreate, UserRead
from app.services.users import (
    UserAlreadyExistsError,
    create_user,
    delete_user,
    get_user,
    list_users,
)


router = APIRouter(prefix="/users", tags=["users"])
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user_in: UserCreate, session: SessionDep) -> UserRead:
    try:
        return create_user(session, user_in)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")


@router.get("", response_model=list[UserRead])
def list_users_endpoint(
    session: SessionDep,
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> list[UserRead]:
    return list_users(session, offset=offset, limit=limit)


@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, session: SessionDep) -> UserRead:
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, session: SessionDep) -> Response:
    user = delete_user(session, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
