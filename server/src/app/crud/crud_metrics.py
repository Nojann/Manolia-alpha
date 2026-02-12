from sqlmodel import Session, select

from src.app.models.metric import Metric
from src.app.models.question import Question
from src.app.database import engine

def create_metric(metric: Metric):
    with Session(engine) as session:
        session.add(metric)
        session.commit()
        session.refresh(metric)
    return metric
        
def read_metrics(question):
    with Session(engine) as session:
        statement = select(Metric).where(Metric.question_id == question.id)
        results = session.exec(statement)
        metrics = results.all()
    return metrics

def read_metric(metric_id: int):
    with Session(engine) as session:
        metric = session.get(Metric, metric_id)
    return metric

def delete_metric(metric_id: int):
    with Session(engine) as session:
        metric = session.get(Metric, metric_id)
        session.delete(metric)
        session.commit()
