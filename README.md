
## 📑 Förslag på README-struktur

### 1. **Titel och kort beskrivning**

> # AI Movie Recommender
>
> Ett Python-projekt som använder AI för att tolka vad du gillar för filmer och rekommenderar titlar från TMDb API.

---

### 2. **Funktioner**

Lista vad projektet kan göra.

* Användaren skriver vad för filmer de gillar (fri text).
* AI tolkar texten och hittar relevanta nyckelord.
* OMDb API hämtar filmer baserat på sökningen.
* Resultaten visas i ett GUI/webbapp med titel, poster och betyg.

---

### 3. **Installation**

Hur man kör projektet.
```bash
# Klona projektet
git clone git@github.com:Zaitex89/Grupp2.git
cd Grupp2

# Installera beroenden
pip install -r requirements.txt

# Kör appen
återkommer
```

---

### 4. **Tekniker & API:er**

Lista vilka ni använder.

* **Programspråk:** Python 3.x
* **Bibliotek:** requests, flask, unittest.mock
* **AI:** OpenAI API (GPT-4) / Hugging Face Transformers
* **Filmdata:** OMDb API

---

### 5. **Användning**

Visa hur programmet funkar med exempel.

* Starta appen
* Skriv in: *“Jag gillar sci-fi med rymdresor”*
* Appen visar en lista på filmer (t.ex. Interstellar, Gravity).

(Bonus: inkludera en GIF eller skärmbild på GUI:t).

---

### 6. **Struktur (mapp & filer)**

![FlowChart](images/flowchart.png)


EXEMPEL:

Förklara hur projektet är organiserat.

```
ai-movie-recommender/
│
├── 
├── 
├── 
├── 
├── 
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
* Andre = tei312    
* Allan = AllanAkkus
---

### 8. **Vem har gjort vad**

Alex 
```
-hela omdb folder
-tests folder -> test_omdb_client.py
-.env
-main.py
-README.md strukturen

```





