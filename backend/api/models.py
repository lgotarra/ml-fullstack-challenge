from pydantic import BaseModel, Field, validator
import re

TEXT_FIELD = Field(..., max_length=500)

# Regex for valid text (letters, numbers, punctuation, basic whitespace)
VALID_TEXT_REGEX = re.compile(r"^[\w\d\s.,!?¿¡'\"-]+$")


class TextValidatedModel(BaseModel):
    text: str = TEXT_FIELD

    @validator("text")
    def check_valid_text(cls, v):
        if not VALID_TEXT_REGEX.match(v):
            raise ValueError("Invalid characters in text")
        return v


class TranslationRequest(TextValidatedModel):
    language: str


class JeringonzaRequest(TextValidatedModel):
    pass
