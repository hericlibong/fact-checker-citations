import streamlit as st
from nlp_utils import clean_text

st.set_page_config(page_title="Fact Check Citation Application", page_icon="✅")
st.title("Assistant Fact Checker de citations")
with st.container():
    st.subheader("📝 Saisissez une citation")
    citation = st.text_input(
        "Entrez la citation à vérifier",
        placeholder="Exemple : 80% des Français sont favorables à la transition énergétique."
    )
    st.caption("💡 Plus la citation est précise, plus les résultats seront fiables.")
    
    if st.button("Vérifier la citation"):
       
        if citation.strip():
            citation_clean = clean_text(citation)
            st.markdown("### Citation soumise à vérification")
            st.info(f"\"{citation.strip()}\"")

            st.markdown("### version nettoyée")
            st.code(citation_clean, language="text")   
        
        else:
            st.warning("⚠️ Veuillez saisir une citation avant de lancer la vérification.")