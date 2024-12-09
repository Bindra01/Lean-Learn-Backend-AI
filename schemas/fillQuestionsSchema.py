from pydantic import BaseModel
from typing import List

class FillQuestionSchema(BaseModel):
    id: str
    question: str
    choices: List[str]
    correct_answer: str
    used: bool