import transformers
from transformers import AutoModelForSeq2SeqLM
from pipelines1 import pipeline

def generate(text):
    nlp = pipeline("e2e-qg", model="valhalla/t5-small-e2e-qg")
    return nlp(text)
