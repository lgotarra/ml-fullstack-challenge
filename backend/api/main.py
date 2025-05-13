from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from api.models import TranslationRequest, JeringonzaRequest
from api.services.translation_service import get_translation
from api.services.jeringonza_service import get_jeringonza

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

if ENVIRONMENT == "development":
    app.add_middleware(
        CORSMiddleware,
        # Allow default Vue.js dev server
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


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
