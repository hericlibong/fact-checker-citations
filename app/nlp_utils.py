import re
import string
import spacy
from strongs_words import STRONGS_WORDS

nlp = spacy.load("fr_core_news_md")

def score_verifiabilite(citation: str) -> tuple[int, dict]:
    """
    Attribue un score de 'vérifiabilité' à la citation selon plusieurs critères :
    - Chiffres détectés
    - Entités nommées
    - Verbes affirmatifs forts
    - Longueur raisonnable
    - Présence de dates

    Retourne un tuple (score_total, détails_par_critère)
    """
    score = 0
    details = {}

    doc = nlp(citation)

    # Critère 1 : Présence de chiffres
    chiffres = [token for token in doc if token.like_num]
    if chiffres:
        score += 2
        details["chiffres"] = f"{len(chiffres)} chiffre(s) détecté(s)"
    else:
        details["chiffres"] = "Aucun chiffre"

    # Critère 2 : Entités nommées (personnes, lieux, organisations)
    entites_cles = [ent for ent in doc.ents if ent.label_ in ["PER", "LOC", "ORG"]]
    if entites_cles:
        score += 2
        details["entites_nommees"] = f"{len(entites_cles)} entité(s)"
    else:
        details["entites_nommees"] = "Aucune"

    # Critère 3 : Verbes affirmatifs forts
    
    

    if any(token.lemma_ in STRONGS_WORDS for token in doc if token.pos_ == "VERB"):
        score += 1
        details["verbe_fort"] = "Présent"
    else:
        details["verbe_fort"] = "Absent"

    # Critère 4 : Longueur raisonnable
    nb_mots = len([token.text for token in doc if token.is_alpha])
    if nb_mots <= 25:
        score += 1
        details["longueur"] = f"{nb_mots} mots ✅"
    else:
        details["longueur"] = f"{nb_mots} mots ❌"

    # Critère 5 : Présence d'une date (entité DATE)
    dates = [ent for ent in doc.ents if ent.label_ == "DATE"]
    if dates:
        score += 1
        details["date"] = f"{len(dates)} date(s) détectée(s)"
    else:
        details["date"] = "Aucune"

    return score, details

def clean_text(text: str) -> str:
    """ minuscules, suppression de la ponctuation, (hors % et chiffres), espaces uniformisés """
    # conversion en minuscules
    text = text.lower()

    # suppression de la ponctuation (hors % et chiffres)
    text = re.sub(rf"[{re.escape(string.punctuation.replace('%', ''))}]", "", text)

    # espaces uniformisés
    text = re.sub(r"\s+", " ", text).strip()

    return text
