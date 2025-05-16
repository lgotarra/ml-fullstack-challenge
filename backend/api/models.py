from pydantic import BaseModel, Field, field_validator
import re

# Regex for valid text (letters, numbers, punctuation, basic whitespace)
VALID_TEXT_REGEX = re.compile(r"^[\w\d\s.,!?¿¡'\"-]+$")


# Defines a model with a text field that is validated using a regular expression to
# ensure it contains only valid characters.
class TextValidatedModel(BaseModel):
    text: str = Field(
        ..., max_length=500, description="Text to be translated or transformed"
    )

    @field_validator("text")
    def check_valid_text(cls, v):
        if not VALID_TEXT_REGEX.match(v):
            raise ValueError("Invalid characters in text")
        return v


class TranslationRequest(TextValidatedModel):
    language: str = Field(
        ..., description="Language for translation (e.g., 'French', 'Spanish', etc.)"
    )


class JeringonzaRequest(TextValidatedModel):
    pass


class TranslationResponse(BaseModel):
    translation: str = Field(
        ..., description="Resulting translated or transformed text"
    )


class HealthResponse(BaseModel):
    status: str = Field(..., description="Current status (e.g., 'ok')")
