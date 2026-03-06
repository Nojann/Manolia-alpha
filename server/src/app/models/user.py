from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    #is_active: bool

    knowledges: list["Knowledge"] = Relationship(back_populates="user", cascade_delete=True) # type: ignore
    questions: list["Question"] = Relationship(back_populates="user", cascade_delete=True) # type: ignore
    metrics: list["Metric"] = Relationship(back_populates="user", cascade_delete=True) # type: ignore

class UserCreate(BaseModel):
    username: str
    plain_password: str