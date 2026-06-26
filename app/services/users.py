from sqlmodel import Session, select

from app.models.user import User
from app.schemas.user import UserCreate


class UserAlreadyExistsError(Exception):
    pass


def create_user(session: Session, user_in: UserCreate) -> User:
    existing_user = session.exec(select(User).where(User.email == str(user_in.email))).first()
    if existing_user:
        raise UserAlreadyExistsError

    user = User(name=user_in.name, email=str(user_in.email))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def list_users(session: Session, offset: int, limit: int) -> list[User]:
    statement = select(User).offset(offset).limit(limit)
    return list(session.exec(statement).all())


def delete_user(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    if not user:
        return None

    session.delete(user)
    session.commit()
    return user
