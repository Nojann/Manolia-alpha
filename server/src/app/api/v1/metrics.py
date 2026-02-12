from fastapi import APIRouter

from src.app.models.metric import Metric
from src.app.models.question import Question
from src.app.crud.crud_metrics import create_metric

router = APIRouter(tags=["metrics"])

@router.post("/metrics/")
def create(question: Question):
    created_metric: Metric = create_metric(question)
    return created_metric
