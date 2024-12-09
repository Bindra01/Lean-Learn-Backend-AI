from pydantic import BaseModel
from typing import List

class mcqSchema(BaseModel):
    id: str
    question: str
    options: List[str]
    answers: List[str]
    used: bool

    