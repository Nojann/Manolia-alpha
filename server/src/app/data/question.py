from sqlmodel import Session, select

from src.app.models.question import Question
from src.app.models.user import User
from src.app.database import engine

def get_question_by_id(question_id: int, user: User):
    with Session(engine) as session:
        statement = select(Question).where(Question.id == question_id, Question.user_id == user.id)
        results = session.exec(statement)
        question = results.first()
    return question

# def get_question_by_id(question_id: int):
#     with Session(engine) as session:
#         question = session.get(Question, question_id)
#     return question

def get_questions(knowledge):
    with Session(engine) as session:
        statement = select(Question).where(Question.knowledge_id == knowledge.id)
        results = session.exec(statement)
        questions = results.all()
    return questions

def create_question(question: Question):
    with Session(engine) as session:
        session.add(question)
        session.commit()
        session.refresh(question)
    return question

def delete_question(question_id: int):
    with Session(engine) as session:
        question = session.get(Question, question_id)
        session.delete(question)
        session.commit()

