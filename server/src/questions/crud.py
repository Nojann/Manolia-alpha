from sqlmodel import Session, select

from src.questions.models import Question
from src.knowledges.models import Knowledge
from src.database import engine

def create_question(Question: Question):
    with Session(engine) as session:
        session.add(Question)
        session.commit()

        
def read_questions(knowledge):
    with Session(engine) as session:
        statement = select(Question).where(Question.knowledge_id == knowledge.id)
        results = session.exec(statement)
        questions = results.all()
    return questions

def read_question(question_id: int):
    with Session(engine) as session:
        question = session.get(Question, question_id)
    return question

# #TODO adapt logic with args
# def update_question(question_id: int, content: str, uri: str):
#     with Session(engine) as session:
#         question = session.get(Question, question_id)
#         question.content = content if content else question.content
#         question.uri = uri if uri else question.uri 
        
#         session.add(question)
#         session.commit()
#         session.refresh(question)

#TODO : test
def delete_question(question_id: int):
    with Session(engine) as session:
        question = session.get(Question, question_id)
        session.delete(question)
        session.commit()

