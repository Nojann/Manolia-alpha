from src.app.models.knowledge import Knowledge
from src.app.crud.crud_knowledges import create_knowledge
from src.app.models.question import Question
from src.app.crud.crud_questions import create_question
from src.app.models.metric import Metric
from src.app.crud.crud_metrics import create_metric

def faker():
    knowledge1 = Knowledge(content="La connaissance est une notion aux sens multiples, à la fois utilisée dans le langage courant et objet d'étude poussée de la part des sciences cognitives et des philosophes contemporains. ", uri="https://fr.wikipedia.org/wiki/Connaissance")
    knowledge2 = Knowledge(content="faculté mentale produisant une assimilation par l'esprit d'un contenu objectif préalablement traduit en signes et en idées ;", uri="https://fr.wikipedia.org/wiki/Connaissance#D%C3%A9finition")
    knowledge3 = Knowledge(content="Pour l'anthropologue, la première connaissance est celle que les hommes ont d'eux-mêmes et de leur environnement, et qui, dans les sociétés primitives, assure leur survie quotidienne.", uri="https://fr.wikipedia.org/wiki/Connaissance#En_anthropologie")
    
    create_knowledge(knowledge1)
    create_knowledge(knowledge2)
    create_knowledge(knowledge3)

    question1 = Question(knowledge = knowledge1, question = "Quel est le sens du mot connaissance ?")
    question2 = Question(knowledge = knowledge1, question = "Quel est la nature de la connaissance ?")
    question3 = Question(knowledge = knowledge1, question = "Quel est le moyen de la connaissance ?")
    question4 = Question(knowledge = knowledge2, question = "Qu'est ce qu'une faculté mentale ?")
    question5 = Question(knowledge = knowledge3, question = "Qu'est ce qu'une connaissance pour l'anthropologue ?")

    create_question(question1)
    create_question(question2)
    create_question(question3)
    create_question(question4)
    create_question(question5)

    metric1 = Metric(question = question1, need_index = 89)
    metric2 = Metric(question = question2, need_index = 28)
    metric3 = Metric(question = question3, need_index = 12)
    metric4 = Metric(question = question4, need_index = 59)
    metric5 = Metric(question = question5, need_index = 91)

    create_metric(metric1)
    create_metric(metric2)
    create_metric(metric3)
    create_metric(metric4)
    create_metric(metric5)

