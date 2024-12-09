from pydantic import BaseModel

class tfSchema(BaseModel):
    id: str
    question: str
    answer: str
    used: bool
