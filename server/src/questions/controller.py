from src.questions.models import Question
from src.questions.crud import create_question as create_question_model, read_questions as read_questions_model, read_question as read_question_model
from src.knowledges.models import Knowledge

def create_question(knowledge: Knowledge):
    question = Question(knowledge = knowledge, question = "Quel est le sens du mot connaissance ?")
    create_question_model(question)

def read_questions(knowledge):
    return read_questions_model(knowledge)

def read_question(question_id):
    return read_question_model(question_id)