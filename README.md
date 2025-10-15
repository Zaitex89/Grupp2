> # AI Movie Recommender
>
> Ett Python-projekt som använder AI för att tolka vad du gillar för filmer och rekommenderar titlar från OMDb API.

---

### 1. **Funktioner**

Lista vad projektet kan göra.

* Användaren skriver vad för filmer de gillar (formulär + fritext).
* AI tolkar texten och hittar relevanta nyckelord.
* OMDb API hämtar filmer baserat på sökningen.
* Resultaten visas i ett GUI/webbapp med titel, poster och betyg.
* Varje sökning sparas i en lokal databas. I Cli-versionen kan vi se de 10 senaste sökningarna

---

### 2. **Installation**

Hur man kör projektet.
```bash
# Klona projektet
git clone git@github.com:Zaitex89/Grupp2.git
cd Grupp2

# Installera beroenden
pip install -r requirements.txt
skapa .env fil som innehåller OMDB_API_KEY="API NYCKEL HÄR" och OPENAI_API_KEY"API NYCKEL HÄR"

# Kör appen
py app.py (Flask)

alternativt:

py main.py (Cli) 
python main.py för cli versionen
python app.py för flask versionen (du får en länk http://127.0.0.1:5000 som tar dig till hemsidan)

# Pytest
för testning av OMDb clienten kör du pytest tests\test_omdb_client.py
```

---

### 3. **Tekniker & API:er**

* **Programspråk:** Python 3.x
* **Bibliotek:** requests, flask, unittest.mock, sqlite3
* **AI:** OpenAI API (GPT-4) / Hugging Face Transformers
* **Bibliotek:** requirements.txt
* **AI:** OpenAI API (GPT-4)
* **Filmdata:** OMDb API

---

### 4. **Användning**

Visa hur programmet funkar med exempel.
AI ger rekommendation med inspiration från vad som matas in i formuläret (oavsett Flask eller CLI).
Saknas godkänd API-nyckel ges ej en rekommendation från AI. 
Då hämtas istället 5 filmer direkt från OMDb, direkt baserat på vilka ord som angetts i formuläret.

* Starta appen
* Skriv in information som:
    Favorite movie or genre: [filmtitel]
    How are you feeling?: [humör/sinnesstämning]
    Tell us more (optional): [fritext, vilken information som helst]

Om Flask:
* Appen visar en lista på filmer
* Filmtitlarna har tillhörande:
    poster
    info från OMDb
    IMDb rating
    AI kommentar

Om CLI:
* Terminalen visar en lista på filmer
* Filmtitlarna har tillhörande:
    info från OMDb
    IMDb rating
    AI kommentar
* Databas sparar vilka sökningar som har gjorts med tillhörande rekommenderade filmer.

---

### 5. **Struktur (mapp & filer)**

![FlowChart](images/flowchart.png)


```

ai_movie_recommender/
│
├── ai/
│   └── gpt_interpreter.py         # Tolkar användarens input med GPT och genererar AI-kommentarer
├── omdb/
│   └── omdb_client.py             # Hämtar filmdata från OMDb API
├── recommender/
│   └── movie_recommender.py       # Samordnar AI-tolkning, OMDb-sökning och filmrankning
├── templates/
│   ├── index.html                 # Startsida med formulär för användarinput
│   └── results.html               # Visar rekommenderade filmer med AI-kommentarer
├── tests/
│   └── test_omdb_client.py        # Enhetstester för OMDb-klienten
├── app.py                         # Flask-applikationens entrypoint
├── featuresseached.py             # Skapar & hanterar databas med info om tidigare filmsökningar
├── main.py                        # CLI-version av programmet
│
├── requirements.txt               # Lista över beroenden (Flask, requests, etc.)
└── README.md                      # Projektbeskrivning, installation och användning


---

### 6. **Team**

* Alex = Zaitex89
* Patrik = KFCGitten
* Andre = tei312    
* Allan = AllanAkkus

### 7. **Vem har gjort vad**
 
```
Alex
* hela omdb folder
* tests folder -> test_omdb_client.py
* .env
* README.md strukturen och innehåll förutom fil/mapp strukturen

André 
* Hela featuressearched.py 
* Delar av main.py som har koppling till featuressearched.py du ser vilka genom //André
* Databas-hantering

Patrik
* README.md, information
* app.py
* bug-fix
* templates -> index.html, results.html

Allan
* gpt_interpreter.py
* recommender -> movie_recommender.py
* integration av AI

```
