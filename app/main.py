import streamlit as st
from nlp_utils import clean_text, score_verifiabilite

st.set_page_config(page_title="Fact Checker de Citations", page_icon="✅")

st.title("🧠 Assistant Fact Checker de citations")

# Étape 1 : Saisie de la citation
st.header("1️⃣ Entrez une citation à analyser")
citation = st.text_input(
    "Saisissez votre citation",
    placeholder="Exemple : 80% des Français sont favorables à la transition énergétique."
)

if st.button("🔎 Lancer l’analyse") and citation.strip():
    
    st.divider()

    # Étape 2 : Vérifiabilité
    st.header("2️⃣ Analyse de la vérifiabilité")

    # Nettoyage (étape prévue dans notre flow)
    citation_clean = clean_text(citation)

    # Analyse NLP sur la version nettoyée
    score, details = score_verifiabilite(citation_clean)
    pourcentage = round((score / 7) * 100)

    # Interprétation
    if score >= 6:
        niveau = "🔵 Très vérifiable"
    elif score >= 4:
        niveau = "🟡 Partiellement vérifiable"
    else:
        niveau = "🔴 Peu vérifiable"

    # Résultats affichés
    st.metric(label="Score de vérifiabilité", value=f"{score} / 7", delta=f"{pourcentage}%")
    st.success(f"Niveau de vérifiabilité : {niveau}")

    st.caption("ℹ️ Ce score indique à quel point la citation contient des éléments factuels détectables. Il ne mesure pas sa véracité.")

    with st.expander("🔍 Détails par critère"):
        for critere, valeur in details.items():
            st.write(f"• **{critere}** : {valeur}")

    st.divider()

    # Étape 3 : Véracité (placeholder)
    st.header("3️⃣ Vérification de la véracité (à venir)")
    st.info("🔄 Cette étape comparera la citation à des sources externes (Wikipedia, presse, etc.) pour évaluer sa véracité.")
    st.caption("⚠️ Fonctionnalité en cours de développement. Elle sera bientôt disponible.")

elif citation.strip() == "":
    st.warning("⚠️ Veuillez saisir une citation pour lancer l’analyse.")

