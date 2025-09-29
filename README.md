
## 📑 Förslag på README-struktur

### 1. **Titel och kort beskrivning**

En tydlig titel + 2–3 meningar som förklarar projektet.
Ex:

> # AI Movie Recommender
>
> Ett Python-projekt som använder AI för att tolka vad du gillar för filmer och rekommenderar titlar från TMDb API.

---

### 2. **Funktioner**

Lista vad projektet kan göra.

* Användaren skriver vad för filmer de gillar (fri text).
* AI tolkar texten och hittar relevanta nyckelord.
* TMDb API hämtar filmer baserat på sökningen.
* Resultaten visas i ett GUI/webbapp med titel, poster och betyg.
* (Extra) Favoritlista och statistik över genres.

---

### 3. **Installation**

Hur man kör projektet.

```bash
# Klona projektet
git clone https://github.com/user/ai-movie-recommender.git
cd ai-movie-recommender

# Installera beroenden
pip install -r requirements.txt

# Kör appen
python app.py
```

---

### 4. **Tekniker & API:er**

Lista vilka ni använder.

* **Programspråk:** Python 3.x
* **Bibliotek:** requests, streamlit/flask/tkinter, matplotlib, pandas
* **AI:** OpenAI API (GPT-4) / Hugging Face Transformers
* **Filmdata:** TMDb API

---

### 5. **Användning**

Visa hur programmet funkar med exempel.

* Starta appen
* Skriv in: *“Jag gillar sci-fi med rymdresor”*
* Appen visar en lista på filmer (t.ex. Interstellar, Gravity).

(Bonus: inkludera en GIF eller skärmbild på GUI:t).

---

### 6. **Struktur (mapp & filer)**

Förklara hur projektet är organiserat.

```
ai-movie-recommender/
│
├── app.py              # Huvudprogrammet
├── ai_module.py        # AI-del (texttolkning)
├── api_module.py       # API-anrop till TMDb
├── gui.py              # Frontend (GUI/webbapp)
├── extras.py           # Extra funktioner (favoriter, statistik)
│
├── requirements.txt    # Beroenden
├── README.md           # Dokumentation
```

---

### 7. **Team**

Lista gruppmedlemmar + vad de bidrog med.

* Person 1: API-integration
* Person 2: AI-modul
* Person 3: GUI/visualisering
* Person 4: Extra features + integration

* Alex = Zaitex89
* Patrik = KFCGitten
* Andre =
* Allan = 
---

### 8. **Framtida utveckling (valfritt men ger plus)**

Ex:

* Stöd för flera språk.
* Rekommendationer baserat på användarhistorik.
* Integration med Spotify för filmsoundtracks 😄.

