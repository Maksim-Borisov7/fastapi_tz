from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from app.repositories.answer.schemas import AnswerResponse


class QuestionSchemas(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerResponse]

    model_config = ConfigDict(from_attributes=True)

