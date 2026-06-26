from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db import get_session
from app.schemas.project import ProjectCreate, ProjectRead
from app.services.projects import (
    ProjectOwnerNotFoundError,
    create_project,
    get_project,
    list_user_projects,
)
from app.services.users import get_user


router = APIRouter(tags=["projects"])
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/projects", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project_endpoint(project_in: ProjectCreate, session: SessionDep) -> ProjectRead:
    try:
        return create_project(session, project_in)
    except ProjectOwnerNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.get("/projects/{project_id}", response_model=ProjectRead)
def get_project_endpoint(project_id: int, session: SessionDep) -> ProjectRead:
    project = get_project(session, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.get("/users/{user_id}/projects", response_model=list[ProjectRead])
def list_user_projects_endpoint(user_id: int, session: SessionDep) -> list[ProjectRead]:
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return list_user_projects(session, user_id)
