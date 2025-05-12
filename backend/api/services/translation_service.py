import json
from pathlib import Path
from collections import defaultdict
from typing import Dict

TRANSLATIONS_FILE = Path(__file__).parent.parent / "data" / "translations.json"


def load_translations() -> Dict[str, Dict[str, str]]:
    """
    Reads translation data from file and organizes it into a dictionary of dictionaries.
    :return: Returns a dictionary where the keys are strings
    representing translation keys, and the values are dictionaries where the keys are language codes and
    the values are the corresponding translations in that language.
    """
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
