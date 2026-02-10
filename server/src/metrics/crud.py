from sqlmodel import Session, select

from src.metrics.models import Metric
from src.questions.models import Question
from src.database import engine

def create_metric(Metric: Metric):
    with Session(engine) as session:
        session.add(Metric)
        session.commit()

        
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
