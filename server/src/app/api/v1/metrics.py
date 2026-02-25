from fastapi import APIRouter

from src.app.models.metric import Metric
from src.app.crud.crud_metrics import create_metric

router = APIRouter(tags=["metrics"])

@router.post("/metrics/")
def create(metric: Metric):
    created_metric: Metric = create_metric(metric)
    return created_metric
