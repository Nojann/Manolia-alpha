from typing import Annotated
from fastapi import APIRouter, Depends

from src.app.models.metric import Metric, MetricCreate
from src.app.data.metric import create_metric

from src.app.auth.dependancies import get_current_user

router = APIRouter(tags=["metrics"])

@router.post("/metrics/")
def create(metric_data: MetricCreate, current_user: Annotated[str, Depends(get_current_user)]):
    metric: Metric = Metric(question_id = metric_data.question_id, need_index = metric_data.need_index, user = current_user)
    created_metric: Metric = create_metric(metric)
    return created_metric
