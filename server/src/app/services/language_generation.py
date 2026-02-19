import os
import spacy

from openai import OpenAI
from pydantic import BaseModel
from src.app.models.knowledge import Knowledge

language_model_api=os.environ.get("LANGUAGE_MODEL_API")
model_name=os.environ.get("LANGUAGE_MODEL_NAME")

client = OpenAI(
    base_url=language_model_api,
    api_key = "sk-no-key-required"
)

nlp = spacy.load("fr_core_news_sm")

def completion(knowledge: Knowledge):

    context = "Texte : ```" + knowledge.content + "```"
    instruction = "A partir du texte génère 3 questions :"
    prompt = context + "\n" + instruction

    #SLM processing
    response = client.responses.create(
        model=model_name,
        input=[
            {"role": "system", "content": "Question Generation"},
            {"role": "user", "content": prompt}],
        )
    text_response = response.output[0].content[0].text

    #Sentence segmentation
    doc = nlp(text_response)
    sents = list()
    for sentence in doc.sents:
        sents.append(sentence.text)

    #Interrogation sentence detection
    questions = list()
    for sent in sents:
        index_mark = sent.rfind("?")
        if(index_mark > 0):
            questions.append(sent[0:index_mark+1])

    return questions

