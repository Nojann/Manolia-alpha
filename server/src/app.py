from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import create_db_and_tables
#TODO : best practice to manage models import
from src.questions.models import Question
from src.knowledges.models import Knowledge
from src.metrics.models import Metric

#Test
from src.questions.controller import create_question, read_question
from src.knowledges.controller import create_knowledge, read_knowledges, delete_knowledge

#TODO : alternative @app.on_event("startup") ?
@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    create_db_and_tables()
    delete_knowledge()
    yield
    #shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}