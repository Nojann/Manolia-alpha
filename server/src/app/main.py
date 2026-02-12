from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.app.database import create_db_and_tables
#TODO : best practice to manage models import
from src.app.models.question import Question
from src.app.models.knowledge import Knowledge
from src.app.models.metric import Metric

#Test
from src.app.faker_seed import faker

#TODO : alternative @app.on_event("startup") ?
@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    create_db_and_tables()
    faker()
    yield
    #shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}