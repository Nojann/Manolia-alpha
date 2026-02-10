from sqlmodel import Session, select

from src.knowledges.models import Knowledge
from src.database import engine

def create_knowledge(knowledge: Knowledge):
    with Session(engine) as session:
        session.add(knowledge)
        session.commit()

def read_knowledges():
    with Session(engine) as session:
        statement = select(Knowledge)
        results = session.exec(statement)
        knowledges = results.all()
    return knowledges

def read_knowledge(knowledge_id: int):
    with Session(engine) as session:
        #statement = select(Knowledge).where(Knowledge.id == knowledge_id)
        #results = session.exec(statement)
        #knowledge = results.first()
        knowledge = session.get(Knowledge, knowledge_id)
    return knowledge

#TODO adapt logic with args
def update_knowledge(knowledge_id: int, content: str, uri: str):
    with Session(engine) as session:
        knowledge = session.get(Knowledge, knowledge_id)
        knowledge.content = content if content else knowledge.content
        knowledge.uri = uri if uri else knowledge.uri 
        
        session.add(knowledge)
        session.commit()
        session.refresh(knowledge)

def delete_knowledge(knowledge_id: int):
    with Session(engine) as session:
        knowledge = session.get(Knowledge, knowledge_id)
        session.delete(knowledge)
        session.commit()
        #TODO : delete join questions