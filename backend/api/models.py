from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(..., max_length=500)
    language: str
