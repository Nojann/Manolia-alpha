from sqlmodel import Field, SQLModel, Relationship
from src.app.models.knowledge import Knowledge

class Question(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question:str

    knowledge_id: int | None = Field(default=None, foreign_key="knowledge.id", ondelete="CASCADE")
    knowledge: Knowledge | None =  Relationship(back_populates="questions")

    metrics: list["Metric"] = Relationship(back_populates="question", cascade_delete=True) # type: ignore
