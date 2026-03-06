from sqlmodel import Session, select

from src.app.models.user import User
from src.app.database import engine

def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

def get_user_by_username(username: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        results = session.exec(statement)
        result = results.first()
    return result

def get_users():
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)
        users = results.all()
    return users

def update_user(user_id: int, username: str, hash: str):
    with Session(engine) as session:
        user = session.get(User, user_id)
        user.username = username if username else user.username
        user.hash = hash if hash else user.hash
    return user

def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()