from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.database import create_db_and_tables

#TODO : best practice to manage models import
from src.app.models.question import Question
from src.app.models.knowledge import Knowledge
from src.app.models.metric import Metric
from src.app.models.user import User

from .api import router

#Test
from src.app.faker_seed import faker

load_dotenv()

#TODO : alternative @app.on_event("startup") ?
@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    create_db_and_tables()
    yield
    #shutdown

app = FastAPI(lifespan=lifespan)
app.include_router(router)

origin = os.environ.get("ORIGIN")
origins = [origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)