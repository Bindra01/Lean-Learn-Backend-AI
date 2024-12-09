from pydantic import BaseModel
from typing import List

class mcqSchema(BaseModel):
    id: str
    question: str
    options: List[str]
    correct_option: str
    used: bool

    