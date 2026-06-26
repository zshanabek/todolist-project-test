from sqlmodel import Session, select

from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate


class ProjectOwnerNotFoundError(Exception):
    pass


def create_project(session: Session, project_in: ProjectCreate) -> Project:
    owner = session.get(User, project_in.owner_id)
    if not owner:
        raise ProjectOwnerNotFoundError

    project = Project(
        name=project_in.name,
        description=project_in.description,
        owner_id=project_in.owner_id,
    )
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def get_project(session: Session, project_id: int) -> Project | None:
    return session.get(Project, project_id)


def list_user_projects(session: Session, user_id: int) -> list[Project]:
    statement = select(Project).where(Project.owner_id == user_id)
    return list(session.exec(statement).all())
