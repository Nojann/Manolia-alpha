import os
from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

database_uri=os.environ.get("DATABASE_URI")

connect_args = {"check_same_thread": False}
engine = create_engine(database_uri, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session