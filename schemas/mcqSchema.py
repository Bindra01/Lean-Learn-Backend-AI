from pydantic import BaseModel
from typing import List

class mcqSchema(BaseModel):
    id: str
    subject: str
    topic: str
    question: str
    options: List[str]
    answers: List[str]
    resource: List[str]
    used: bool

    