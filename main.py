from fastapi import FastAPI
from api.mcqQuestionRouter import router as mcq_router
from api.tfQuestionRouter import router as tf_router
from api.fillQUestionRouter import router as fill_router

app = FastAPI()
app.include_router(tf_router)
app.include_router(mcq_router)
app.include_router(fill_router)