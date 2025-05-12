from api.models import TranslationRequest
from fastapi import FastAPI, HTTPException
from api.translation_service import get_translation
import re

app = FastAPI()

# Allow only letters, numbers, punctuation and basic whitespace
VALID_TEXT_REGEX = re.compile(r"^[\w\d\s.,!?¿¡'\"-]+$")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate")
def translate(request: TranslationRequest):
    if not VALID_TEXT_REGEX.match(request.text):
        raise HTTPException(status_code=400, detail="Invalid characters in text")

    translation = get_translation(request.text, request.language)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported text or language")

    return {"translation": translation}
