# Assistant Fact-Checker de Citations


---

## 📝 Étape suivante : Complétons le `README.md`

Je te propose une **première version structurée**, claire et concise, que tu pourras modifier ou étoffer au fil du projet :

---

### 📄 `README.md` – version 1

```markdown
# Assistant Fact-Checker de Citations

Ce projet est un outil d’aide à la vérification de citations, destiné aux journalistes, blogueurs ou rédacteurs souhaitant s’assurer de la véracité d’une citation avant publication.

L'utilisateur peut entrer une citation, et l'outil interroge automatiquement des sources fiables comme Wikipedia pour retrouver des correspondances, analyser le contexte, et retourner un score de similarité sémantique.

---

## 🎯 Objectifs

- Aider à valider ou infirmer une citation avec des sources fiables.
- Fournir des extraits de contexte autour de la citation.
- Évaluer le degré de correspondance avec les sources.
- Sauvegarder un historique des vérifications.

---

## 🧰 Stack technique

- Python 3.10+
- Streamlit (interface)
- Wikipedia API (source principale)
- SentenceTransformers (`paraphrase-MiniLM`) – similarité sémantique
- spaCy – extraction entités et mots-clés
- JSON ou SQLite (persistance)

---

## 📦 Installation (local)

```bash
git clone https://github.com/<ton-utilisateur>/fact-checker-citations.git
cd fact-checker-citations
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

---

## 🚀 Lancer l’application

```bash
streamlit run app/main.py
```

---

## 📌 TODOs

- [ ] Interface utilisateur Streamlit
- [ ] Prétraitement des citations
- [ ] Connexion aux APIs (Wikipedia, autres)
- [ ] Calcul de similarité sémantique
- [ ] Interface résultats + score
- [ ] Persistance historique
- [ ] Démo déployée

---

## 📃 Licence

Ce projet est open-source, sous licence MIT.
```

---
