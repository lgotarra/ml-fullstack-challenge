from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from api.models import (
    HealthResponse,
    TranslationRequest,
    JeringonzaRequest,
    TranslationResponse,
)
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


@app.get("/", summary="Root Endpoint", response_model=dict)
def read_root():
    """
    Root endpoint to verify the API is running.
    """
    return {"Hello": "World"}


@app.get("/healthz", summary="Health Check", response_model=HealthResponse)
def health_check():
    """
    Returns basic health status of the API.
    """
    return {"status": "ok"}


@app.get("/ready", summary="Readiness Check", response_model=HealthResponse)
def readiness_check():
    """
    Indicates whether the API is ready to handle requests.
    """
    return {"status": "ready"}


@app.post("/translate", summary="Translate Text", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    """
    Translates the given text into the specified language.
    - text: The input text to translate.
    - language: The target language code (e.g., 'French', 'Spanish', etc.).
    """
    translation = get_translation(request.text, request.language)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported text or language")

    return {"translation": translation}


@app.post(
    "/jeringonza", summary="Convert to Jeringonza", response_model=TranslationResponse
)
def jeringonza(request: JeringonzaRequest):
    """
    Applies the Jeringonza language transformation to the input text.
    - text: The input text to transform.
    """
    translation = get_jeringonza(request.text)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported text or language")

    return {"translation": translation}
