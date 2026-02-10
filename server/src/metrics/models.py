from sqlmodel import Field, SQLModel
#TODO : add pydantic validation

class Metric(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question_id: int | None = Field(default=None, foreign_key="question.id", ondelete="CASCADE")
    need_index: int
