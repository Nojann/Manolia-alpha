from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from src.app.auth.dependancies import get_current_user

from src.app.models.knowledge import Knowledge, KnowledgeCreate
from src.app.models.question import Question

from src.app.data.knowledge import create_knowledge, get_knowledges_by_user, get_knowledge_by_id
#from src.app.data.knowledge update_knowledge, delete_knowledge
from src.app.data.question import get_questions, create_question

from src.app.services.language_generation import questions_generation

#Added in __ini__
router = APIRouter(tags=["knowledges"])

@router.get("/knowledges/")
def read(current_user: Annotated[str, Depends(get_current_user)]):
    knowledges = get_knowledges_by_user(current_user)
    return knowledges

@router.get("/knowledges/{id}")
def read(id: int, current_user: Annotated[str, Depends(get_current_user)]):
    knowledge = get_knowledge_by_id(id, current_user)
    return knowledge

@router.post("/knowledges/")
def create(knowledge_data: KnowledgeCreate, current_user: Annotated[str, Depends(get_current_user)]):
    knowledge = Knowledge(content=knowledge_data.content, uri=knowledge_data.uri, user=current_user)
    created_knowledge = create_knowledge(knowledge)
    # if created_knowledge is None:
    #     raise NotFoundException("Failed to create knowledge")
    return created_knowledge

@router.post("/knowledges/{id}/questions")
def generate_questions(id: int, current_user: Annotated[str, Depends(get_current_user)]):
    knowledge: Knowledge = get_knowledge_by_id(id, current_user)
    if not knowledge:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden. The requested knowledge is not available for the provided ID.",
            headers={"WWW-Authenticate": "Bearer"},
    )
    questions_raw = questions_generation(knowledge)
    for q in questions_raw:
        question = Question(question = q, knowledge=knowledge)
        create_question(question)
    return questions_raw

@router.get("/knowledges/{id}/questions")
def read_questions(id: int, current_user: Annotated[str, Depends(get_current_user)]):
    knowledge: Knowledge = get_knowledge_by_id(id, current_user)
    if not knowledge:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden. The requested knowledge is not available for the provided ID.",
            headers={"WWW-Authenticate": "Bearer"},
    )
    questions = get_questions(knowledge)
    return questions

#TODO: adapt with correct pattern
# @router.post("/knowledges/{id}")
# def update(id: int, content: str, uri: str):
#     knowledge = update_knowledge(id, content, uri)
#     return knowledge

# @router.delete("/knowledges/{id}")
# def delete(id: int):
#     knowledge = delete_knowledge(id)
#     return knowledge