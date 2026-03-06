from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel
from src.app.models.user import User

class Knowledge(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    uri: str = Field(index=True)

    questions: list["Question"] = Relationship(back_populates="knowledge", cascade_delete=True) # type: ignore

    user_id: int | None = Field(default=None, foreign_key="user.id", ondelete="CASCADE")
    user: User | None =  Relationship(back_populates="knowledges")

class KnowledgeCreate(BaseModel):
    content: str
    uri:str