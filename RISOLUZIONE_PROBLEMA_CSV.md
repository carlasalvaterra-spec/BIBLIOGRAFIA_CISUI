# ⚠️ RISOLUZIONE PROBLEMA: "Impossibile caricare il file CSV"

## 🔍 Perché succede?

Quando apri il file HTML **direttamente dal computer** (facendo doppio clic), il browser lo apre con protocollo `file://` che blocca il caricamento del CSV per motivi di sicurezza (policy CORS).

**Questo è NORMALE e succede a tutti!** ✅

---

## ✅ SOLUZIONI (3 metodi)

### 🏆 SOLUZIONE 1: Carica su GitHub Pages (CONSIGLIATA)

**Questo è il metodo definitivo - funzionerà sempre!**

Una volta caricato su GitHub e attivato GitHub Pages, il problema sparisce perché il sito è servito via `https://` e non `file://`.

**Passi:**
1. Carica entrambi i file su GitHub:
   - `bibliografia_ricercabile_csv.html`
   - `bibliografia_cisui.csv`
2. Attiva GitHub Pages (Settings → Pages)
3. Visita l'URL: `https://[username].github.io/[repo]/bibliografia_ricercabile_csv.html`

✅ **Funzionerà perfettamente!**

---

### 💻 SOLUZIONE 2: Usa un server locale (per testare prima di caricare)

Ho preparato degli script per avviare un mini-server sul tuo computer:

#### **Per Windows:**
1. Metti questi 3 file nella stessa cartella:
   - `bibliografia_ricercabile_csv.html`
   - `bibliografia_cisui.csv`
   - `avvia_server.bat`
2. **Doppio clic** su `avvia_server.bat`
3. Si apre automaticamente il browser con la bibliografia funzionante!

#### **Per Mac/Linux:**
1. Metti questi 3 file nella stessa cartella:
   - `bibliografia_ricercabile_csv.html`
   - `bibliografia_cisui.csv`
   - `avvia_server.py`
2. Apri il Terminale nella cartella
3. Esegui: `python3 avvia_server.py`
4. Si apre automaticamente il browser!

**Requisito:** Devi avere Python installato (è già preinstallato su Mac/Linux)

---

### 🌐 SOLUZIONE 3: Usa estensione browser (più semplice)

Se hai **Google Chrome** o **Firefox**:

#### Chrome:
1. Installa l'estensione: **"Web Server for Chrome"** o **"Allow CORS"**
2. Configura per permettere l'accesso ai file locali
3. Riapri l'HTML

#### Firefox:
1. Apri Firefox
2. Digita nella barra: `about:config`
3. Cerca: `privacy.file_unique_origin`
4. Imposta a `false`
5. Riavvia Firefox

⚠️ **Attenzione**: Questo metodo riduce la sicurezza del browser. Ricordati di ripristinare dopo!

---

### 🔧 SOLUZIONE 4: Metodo manuale veloce (Python in una riga)

Se hai Python installato:

#### Windows:
1. Apri **Prompt dei comandi** nella cartella con i file
2. Esegui:
   ```
   python -m http.server 8000
   ```
3. Apri browser su: `http://localhost:8000/bibliografia_ricercabile_csv.html`

#### Mac/Linux:
1. Apri **Terminale** nella cartella con i file
2. Esegui:
   ```
   python3 -m http.server 8000
   ```
3. Apri browser su: `http://localhost:8000/bibliografia_ricercabile_csv.html`

Per fermare: premi `Ctrl+C` nel terminale

---

## 🎯 QUALE SCEGLIERE?

| Soluzione | Quando usarla | Difficoltà |
|-----------|---------------|------------|
| **GitHub Pages** | Sempre (versione finale) | ⭐ Facile |
| **Script server** | Per testare modifiche localmente | ⭐⭐ Media |
| **Estensione browser** | Test rapidi | ⭐⭐ Media |
| **Python manuale** | Se sai usare il terminale | ⭐⭐⭐ Avanzata |

---

## 💡 CONSIGLIO:

**Per lavorare:**
1. Usa **SOLUZIONE 2** (script server) per testare le modifiche sul tuo computer
2. Quando sei soddisfatto, carica tutto su **GitHub Pages**
3. Da quel momento in poi, funzionerà sempre online senza problemi!

---

## ❓ FAQ

**Q: Ma sulla versione precedente (senza CSV) funzionava in locale!**  
A: Sì, perché i dati erano dentro l'HTML. Con il CSV separato, il browser deve "caricare un file esterno" e questo richiede un server web.

**Q: I miei colleghi avranno lo stesso problema?**  
A: No! Una volta su GitHub Pages, i tuoi colleghi modificheranno solo il CSV su GitHub. Non devono testare nulla in locale.

**Q: È complicato per noi...**  
A: Capisco! Allora ti consiglio di:
   - Usare la versione **SENZA CSV** per testare in locale
   - Usare la versione **CON CSV** solo su GitHub Pages
   
   Oppure usa gli script che ho preparato - sono semplicissimi! Solo doppio clic.

**Q: Posso avere una versione che funzioni anche in locale senza server?**  
A: Sì! Posso creare una versione "ibrida" che ha i dati sia dentro l'HTML (per test locali) che legge il CSV se disponibile (per GitHub). Vuoi che la faccia?

---

## 🆘 SERVE ANCORA AIUTO?

Dimmi:
- Che sistema operativo usi? (Windows, Mac, Linux)
- Preferisci testare in locale o caricare direttamente su GitHub?
- Hai Python installato sul computer?

Ti guido passo-passo! 😊
