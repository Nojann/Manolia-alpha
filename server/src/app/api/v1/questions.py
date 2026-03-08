from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from src.app.auth.dependancies import get_current_user

from src.app.models.question import Question
from src.app.models.metric import Metric, MetricCreate

from src.app.data.question import get_question_by_id
from src.app.data.metric import get_metrics, create_metric

#Added in __ini__
router = APIRouter(tags=["questions"])

@router.get("/questions/{id}/metrics")
def read_questions(id: int, current_user: Annotated[str, Depends(get_current_user)]):
    question: Question = get_question_by_id(id, current_user)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden. The requested knowledge is not available for the provided ID.",
            headers={"WWW-Authenticate": "Bearer"},
    )
    metrics = get_metrics(question)
    return metrics

@router.post("/questions/{id}/metrics")
def create(id: int, metric_data: MetricCreate, current_user: Annotated[str, Depends(get_current_user)]):
    question: Question = get_question_by_id(id, current_user)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden. The requested knowledge is not available for the provided ID.",
            headers={"WWW-Authenticate": "Bearer"},
    )
    metric: Metric = Metric(question_id = id, need_index = metric_data.need_index, user = current_user)
    created_metric: Metric = create_metric(metric)
    return created_metric