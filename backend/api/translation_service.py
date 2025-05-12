import json
from pathlib import Path
from collections import defaultdict
from typing import Dict

TRANSLATIONS_FILE = Path(__file__).parent / "data" / "translations.json"


def load_translations() -> Dict[str, Dict[str, str]]:
    with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    data = defaultdict(dict)
    for item in raw_data:
        data[item["key"]][item["language"]] = item["translation"]
    return dict(data)


# Load at startup
translations = load_translations()


def get_translation(text: str, language: str) -> str:
    try:
        return translations[text][language]
    except KeyError:
        return None
