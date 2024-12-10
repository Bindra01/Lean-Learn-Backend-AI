from pydantic import BaseModel

class tfSchema(BaseModel):
    id: str
    topic: str
    question: str
    answer: str
    resource: str
    used: bool
