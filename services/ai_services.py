from ai.gemini_llm import generate_details
from schemas.aiSchema import WrongAnswerSchema

def get_explaination(wrongAnswer):
    return generate_details(wrongAnswer)

def get_report(question: str):
    return generate_details(question)