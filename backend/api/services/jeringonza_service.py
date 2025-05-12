def get_jeringonza(text: str) -> str:
    """
    Convert text to Jeringonza.
    """
    # Define the rules for Jeringonza
    vowels = "aeiou"
    jeringonza = ""

    for char in text:
        if char.lower() in vowels:
            jeringonza += char + "p" + char
        else:
            jeringonza += char

    return jeringonza
