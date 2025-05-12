vowels = "aeiouáéíóúü"
critical_consonants = "gq"


def is_silent_vowel(text: str, index: int) -> bool:
    """
    Check if the vowel at the given index is silent.
    """

    # Check if the index is valid
    if index < 0 or index >= len(text):
        return False

    current_char = text[index].lower()

    # If it's not a vowel, return False
    if current_char not in vowels:
        return False

    # Special case: "ü" is not silent
    if current_char == "ü":
        return False

    # For other vowels, consider them silent if preceded by a critical consonant
    if index > 0 and text[index - 1].lower() in critical_consonants:
        return True

    return False


def get_jeringonza(text: str) -> str:
    """
    Convert text to Jeringonza.
    """
    jeringonza = ""

    for idx, char in enumerate(text):
        if char.lower() in vowels:
            if is_silent_vowel(text, idx):
                jeringonza += char
            else:
                jeringonza += char + "p" + char.lower()
        else:
            jeringonza += char

    return jeringonza
