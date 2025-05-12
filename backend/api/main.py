from fastapi import FastAPI, HTTPException
import re
from api.models import TranslationRequest, JeringonzaRequest
from api.services.translation_service import get_translation
from api.services.jeringonza_service import get_jeringonza

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate")
def translate(request: TranslationRequest):
    translation = get_translation(request.text, request.language)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported text or language")

    return {"translation": translation}


@app.post("/jeringonza")
def jeringonza(request: JeringonzaRequest):
    translation = get_jeringonza(request.text)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported text or language")

    return {"translation": translation}
