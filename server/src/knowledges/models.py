from sqlmodel import Field, SQLModel, Relationship
#TODO : add pydantic validation

class Knowledge(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    uri: str = Field(index=True)

    questions: list["Question"] = Relationship(back_populates="knowledge", cascade_delete=True) # type: ignore