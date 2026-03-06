from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel
from src.app.models.question import Question
from src.app.models.user import User

class Metric(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    question_id: int | None = Field(default=None, foreign_key="question.id", ondelete="CASCADE")
    question: Question | None =  Relationship(back_populates="metrics")
    
    need_index: int

    user_id: int | None = Field(default=None, foreign_key="user.id", ondelete="CASCADE")
    user: User | None =  Relationship(back_populates="metrics")

class MetricCreate(BaseModel):
    question_id: int
    need_index: int