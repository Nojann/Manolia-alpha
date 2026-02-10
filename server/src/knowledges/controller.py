from src.knowledges.models import Knowledge
from src.knowledges.crud import create_knowledge as create_knowledge_model, read_knowledges as read_knowledges_model, read_knowledge as read_knowledge_model, update_knowledge as update_knowledge_model, delete_knowledge as delete_knowledge_model

def create_knowledge():
    connaissance = Knowledge(content="La connaissance n'est pas.", uri="https://perdu.fr")
    create_knowledge_model(connaissance)
    return read_knowledges()[-1]

def read_knowledges():
    return read_knowledges_model()

def read_knowledge(knowledge_id):
    return read_knowledge_model(knowledge_id)

def update_knowledge():
    return update_knowledge_model(2, "faculté mentale produisant une assimilation par l'esprit d'un contenu objectif préalablement traduit en signes et en idées ;", "https://fr.wikipedia.org/wiki/Connaissance#D%C3%A9finition")

def delete_knowledge():
    return delete_knowledge_model(7)
