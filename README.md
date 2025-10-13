> # AI Movie Recommender
>
> Ett Python-projekt som använder AI för att tolka vad du gillar för filmer och rekommenderar titlar från OMDb API.

---

### 1. **Funktioner**

Lista vad projektet kan göra.

* Användaren skriver vad för filmer de gillar (fri text).
* AI tolkar texten och hittar relevanta nyckelord.
* OMDb API hämtar filmer baserat på sökningen.
* Resultaten visas i ett GUI/webbapp med titel, poster och betyg.

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
python main.py för cli versionen
python app.py för flask versionen (du får en länk http://127.0.0.1:5000 som tar dig till hemsidan)

# Pytest
för testning av OMDb clienten kör du pytest tests\test_omdb_client.py
```

---

### 3. **Tekniker & API:er**

* **Programspråk:** Python 3.x
* **Bibliotek:** requirements.txt
* **AI:** OpenAI API (GPT-4)
* **Filmdata:** OMDb API

---

### 4. **Användning**

* Starta appen
* Skriv in: *“I like sci fi movies”*
* main.py visar en lista på filmer (t.ex. Interstellar, Alien).
* appy visar då istället film omslagen



---

### 5. **Struktur (mapp & filer)**

![FlowChart](images/flowchart.png)



Förklarar hur projektet är organiserat.

```
GRUPP2
├── ai chat gpt interpreter
├── images # Bilder för README.md 
├── omdb # Hämtar api från OMDb och skickar den vidare
├── recommender # film rekommenderaren
├── templates # html
├── tests #pytest
├── .env # Behöver skapa en lokalt
├── requirements.txt    # Beroenden
├── README.md           # Dokumentation
```


---

### 6. **Team**

Lista gruppmedlemmar 

* Alex = Zaitex89
* Patrik = KFCGitten
* Andre = tei312    
* Allan = AllanAkkus
---

### 7. **Vem har gjort vad**

Alex 
```
-hela omdb folder
-tests folder -> test_omdb_client.py
-.env
-README.md strukturen och innehåll

```





