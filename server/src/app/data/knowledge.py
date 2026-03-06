from sqlmodel import Session, select

from src.app.models.knowledge import Knowledge
from src.app.models.user import User
from src.app.database import engine

def get_knowledge_by_id(knowledge_id: int, user: User):
    with Session(engine) as session:
        statement = select(Knowledge).where(Knowledge.id == knowledge_id, Knowledge.user_id == user.id)
        results = session.exec(statement)
        knowledge = results.first()
    return knowledge

# def get_knowledge_by_id(knowledge_id: int):
#     with Session(engine) as session:
#         knowledge = session.get(Knowledge, knowledge_id)
#     return knowledge   

# No filter by user
def get_knowledges():
    with Session(engine) as session:
        statement = select(Knowledge)
        results = session.exec(statement)
        knowledges = results.all()
    return knowledges

def get_knowledges_by_user(user: User):
    with Session(engine) as session:
        statement = select(Knowledge).where(Knowledge.user_id == user.id)
        results = session.exec(statement)
        knowledges = results.all()
    return knowledges

def create_knowledge(knowledge: Knowledge):
    with Session(engine) as session:
        session.add(knowledge)
        session.commit()
        session.refresh(knowledge)
    return knowledge

#TODO adapt logic with args
# No filter by user
# Transform to update_knowledge(knowledge: Knowledge)
# def update_knowledge(knowledge_id: int, content: str, uri: str):
#     with Session(engine) as session:
#         knowledge = session.get(Knowledge, knowledge_id)
#         knowledge.content = content if content else knowledge.content
#         knowledge.uri = uri if uri else knowledge.uri 
        
#         session.add(knowledge)
#         session.commit()
#         session.refresh(knowledge)
#     return knowledge

# No filter by user
# def delete_knowledge(knowledge_id: int):
#     with Session(engine) as session:
#         knowledge = session.get(Knowledge, knowledge_id)
#         session.delete(knowledge)
#         session.commit()