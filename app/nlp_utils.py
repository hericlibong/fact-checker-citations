import re
import string

def clean_text(text: str) -> str:
    """ minuscules, suppression de la ponctuation, (hors % et chiffres), espaces uniformisés """
    # conversion en minuscules
    text = text.lower()

    # suppression de la ponctuation (hors % et chiffres)
    text = re.sub(rf"[{re.escape(string.punctuation.replace('%', ''))}]", "", text)

    # espaces uniformisés
    text = re.sub(r"\s+", " ", text).strip()

    return text
