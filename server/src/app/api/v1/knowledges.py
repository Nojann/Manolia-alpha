from typing import Annotated
from fastapi import APIRouter

from src.app.models.knowledge import Knowledge
from src.app.models.question import Question

from src.app.data.knowledge import create_knowledge, read_knowledges, read_knowledge, update_knowledge, delete_knowledge
from src.app.data.question import read_questions as read_questions_crud, create_question

from src.app.services.language_generation import questions_generation

#Added in __ini__
router = APIRouter(tags=["knowledges"])

@router.post("/knowledges/")
def create(knowledge: Knowledge):
    created_knowledge = create_knowledge(knowledge)
    # if created_knowledge is None:
    #     raise NotFoundException("Failed to create knowledge")
    return created_knowledge

@router.get("/knowledges/")
def read():
    knowledges = read_knowledges()
    return knowledges

@router.get("/knowledges/{id}")
def read(id: int):
    knowledge = read_knowledge(id)
    return knowledge

#TODO: adapt with correct pattern
@router.post("/knowledges/{id}")
def update(id: int, content: str, uri: str):
    knowledge = update_knowledge(id, content, uri)
    return knowledge

@router.delete("/knowledges/{id}")
def delete(id: int):
    knowledge = delete_knowledge(id)
    return knowledge

@router.post("/knowledges/{id}/questions")
def create_questions(id: int):
    knowledge = read_knowledge(id)
    questions_raw = questions_generation(knowledge)
    for q in questions_raw:
        question = Question(question = q, knowledge=knowledge)
        create_question(question)
    return questions_raw

@router.get("/knowledges/{id}/questions")
def read_questions(id: int):
    knowledge: Knowledge = read_knowledge(id)
    #questions = knowledge.questions
    #TODO : refacto ?
    questions = read_questions_crud(knowledge)
    return questions