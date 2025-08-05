#qna_generator

from transformers import pipeline

def load_qa_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_query(qa_model, question, context):
    result = qa_model(question=question, context=context)
    return result['answer']

