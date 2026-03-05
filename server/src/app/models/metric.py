from sqlmodel import Field, SQLModel, Relationship
from src.app.models.question import Question

class Metric(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    question_id: int | None = Field(default=None, foreign_key="question.id", ondelete="CASCADE")
    question: Question | None =  Relationship(back_populates="metrics")
    
    need_index: int
