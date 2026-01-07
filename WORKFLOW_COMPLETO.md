# 📋 GUIDA COMPLETA: Workflow Ibrido Google Sheets + GitHub

## 🎯 OBIETTIVO

Permettere ai colleghi di lavorare facilmente su Google Sheets mentre mantieni il controllo qualità e il versioning su GitHub prima della pubblicazione.

---

## 🔄 IL WORKFLOW IN 3 PASSI

```
┌─────────────────────────────────────┐
│  FASE 1: LAVORO (Google Sheets)     │
│  Colleghi aggiungono/modificano     │
│  Collaborazione in tempo reale      │
└──────────────┬──────────────────────┘
               │
               │ Export CSV
               ▼
┌─────────────────────────────────────┐
│  FASE 2: CONTROLLO (Tu)             │
│  Verifichi che tutto sia corretto   │
│  Controlli formato e completezza    │
└──────────────┬──────────────────────┘
               │
               │ Upload
               ▼
┌─────────────────────────────────────┐
│  FASE 3: PUBBLICAZIONE (GitHub)     │
│  Sostituisci CSV                    │
│  Commit con messaggio               │
│  Online in 2 minuti                 │
└─────────────────────────────────────┘
```

---

## 📊 FASE 1: Setup Iniziale (UNA TANTUM)

### Step 1: Crea Google Sheets

1. Vai su [sheets.google.com](https://sheets.google.com)
2. **Crea nuovo foglio**
3. Rinominalo: **"CISUI - Bibliografia Master"**

### Step 2: Importa i dati iniziali

1. **File → Importa**
2. Seleziona il file CSV che ti fornirò (quando pronto)
3. **Sostituisci foglio di lavoro corrente**

### Step 3: Formattazione (importante!)

**Applica queste impostazioni per evitare errori:**

#### Colonna A (tipologia):
- **Dati → Validazione dati**
- Seleziona "Elenco da intervallo"
- Inserisci: `articolo in rivista, articolo in volume miscellaneo, volume miscellaneo, monografia`
- ✅ Mostra elenco a discesa nella cella
- ✅ Rifiuta l'input se i dati non sono validi

#### Colonna F (precisazione_curatore):
- **Dati → Validazione dati**
- Elenco: `a cura di, (vuoto)`
- ✅ Questo evita errori di battitura

#### Colonna J (anno):
- **Formato → Numero → Numero**
- Nessun decimale

#### Intestazioni (riga 1):
- **Formato → Testo → Grassetto**
- **Sfondo:** Rosso bordeaux (#9d2235)
- **Testo:** Bianco

### Step 4: Protezione intestazioni

1. Seleziona la **riga 1** (intestazioni)
2. **Dati → Proteggi fogli e intervalli**
3. **Imposta autorizzazioni:** "Solo tu puoi modificare"
4. Questo impedisce cancellazioni accidentali

### Step 5: Condivisione

1. **Pulsante "Condividi"** (in alto a destra)
2. Aggiungi email dei colleghi
3. **Permesso:** "Editor" (possono modificare)
4. **Messaggio:** "Foglio per aggiornamenti bibliografia CISUI"
5. **Invia**

---

## 👥 FASE 2: Lavoro Quotidiano dei Colleghi

### Istruzioni per i colleghi:

#### Come aggiungere una nuova pubblicazione:

1. **Vai all'ultima riga piena**
2. **Premi invio** per creare nuova riga
3. **Compila tutte le colonne obbligatorie:**
   - tipologia (usa menu a tendina)
   - autore o titolo (a seconda del tipo)
   - anno
   - altri campi rilevanti

4. **NON lasciare celle vuote** nelle colonne obbligatorie
5. **Usa le tendine** dove disponibili (evitano errori)

#### Come modificare una pubblicazione esistente:

1. **Cerca** la riga (Ctrl+F)
2. **Clicca sulla cella** da modificare
3. **Modifica** il contenuto
4. **Salvataggio automatico** ✅

#### ⚠️ COSA NON FARE:

- ❌ NON cancellare la riga di intestazione
- ❌ NON cambiare l'ordine delle colonne
- ❌ NON inserire colonne nuove (chiedi prima)
- ❌ NON usare formule nelle celle dati

---

## 🔍 FASE 3: Controllo Qualità (TU)

### Quando i colleghi ti avvisano che hanno finito:

#### Step 1: Controllo visivo rapido

Apri il foglio e controlla:
- [ ] Nessuna riga con celle vuote nelle colonne obbligatorie
- [ ] Tipologie scritte correttamente (grazie alle tendine dovrebbe essere ok)
- [ ] Anni sono numeri (non testo tipo "duemilaquattro")
- [ ] Nomi curatori hanno "(a cura di)" dove necessario

#### Step 2: Usa filtri per verificare

1. **Seleziona tutto** (Ctrl+A)
2. **Dati → Crea un filtro**
3. **Clicca freccia su "tipologia"** → Verifica che ci siano solo i 4 tipi validi
4. **Clicca freccia su "anno"** → Controlla anomalie (es. anno 0, anno futuro)

#### Step 3: Cerca duplicati

1. **Dati → Rimuovi duplicati** (solo per vedere, non confermare)
2. Se trova duplicati, verifica se sono errori

---

## 📥 FASE 4: Export e Pubblicazione

### Step 1: Esporta da Google Sheets

1. **File → Scarica → Valori separati da virgola (.csv)**
2. Il file si salva come: `CISUI - Bibliografia Master.csv`
3. **Rinominalo** in: `bibliografia_cisui_completo.csv`

### Step 2: Verifica il CSV (opzionale ma consigliato)

1. Apri con Notepad++ o simile
2. Verifica che:
   - Prima riga = intestazioni
   - Nessuna riga vuota
   - Separatore = virgola
   - Encoding = UTF-8

### Step 3: Test locale (se vuoi testare prima)

1. Metti CSV nella cartella con `bibliografia_ricercabile_completo.html`
2. Avvia server locale (`avvia_server.bat`)
3. Verifica che tutto funzioni
4. Se ok, procedi con GitHub

### Step 4: Carica su GitHub

#### Metodo A: Via interfaccia web (PIÙ SEMPLICE)

1. Vai sul repository: `https://github.com/bibliografiacisui/bibliografiacisui`
2. **Clicca** sul file `bibliografia_cisui_completo.csv`
3. **Clicca** sull'icona **✏️ Edit** (matita in alto a destra)
4. **Seleziona tutto** (Ctrl+A) e **cancella**
5. **Apri** il nuovo CSV con Notepad
6. **Copia tutto** (Ctrl+A, Ctrl+C)
7. **Incolla** nel editor GitHub
8. **Scorri in basso** alla sezione "Commit changes"
9. **Messaggio commit:** (es. "Aggiornamento bibliografia: aggiunti 25 nuovi titoli")
10. **Descrizione estesa** (opzionale): dettagli su cosa è cambiato
11. **Commit changes** (pulsante verde)

#### Metodo B: Via delete + upload (ALTERNATIVO)

1. **Clicca** su `bibliografia_cisui_completo.csv`
2. **Clicca** sui tre puntini `...` in alto a destra
3. **Delete file**
4. Conferma cancellazione
5. **Add file → Upload files**
6. **Trascina** il nuovo CSV
7. **Commit changes**

---

## ⏱️ TEMPISTICHE

| Azione | Tempo | Frequenza |
|--------|-------|-----------|
| Colleghi aggiungono titoli | 2-5 min | Quando serve |
| Tu controlli | 5 min | Settimanale? |
| Tu pubblichi | 2 min | Dopo controllo |
| GitHub pubblica | 2 min | Automatico |

**Totale:** ~10 minuti ogni aggiornamento

---

## 🆘 TROUBLESHOOTING

### "Ho fatto pasticci su Google Sheets!"

**Soluzione 1: Cronologia versioni**
1. **File → Cronologia delle versioni → Vedi cronologia delle versioni**
2. Seleziona una versione precedente
3. **Ripristina questa versione**

**Soluzione 2: Non hai ancora pubblicato su GitHub?**
- Nessun problema! Non è online, risolvi su Sheets

**Soluzione 3: Hai già pubblicato su GitHub?**
- Rollback GitHub (vedi sotto)

### "Ho pubblicato un CSV sbagliato su GitHub!"

1. Vai sul repository GitHub
2. Clicca su **`bibliografia_cisui_completo.csv`**
3. Clicca su **History** (orologio in alto a destra)
4. Trova l'ultima versione corretta
5. Clicca sui **tre puntini** → **View file**
6. Copia tutto il contenuto
7. Torna al file attuale → Edit → Incolla
8. Commit: "Rollback a versione precedente"

### "Il sito non si aggiorna dopo il commit!"

- Aspetta 2-5 minuti (GitHub Pages impiega tempo)
- Prova hard refresh: **Ctrl+F5**
- Prova in **finestra anonima**
- Verifica che GitHub Pages sia attivo (Settings → Pages)

### "Google Sheets non esporta correttamente"

- Usa "Valori separati da virgola (.csv)" NON "CSV UTF-8"
- Verifica che non ci siano formule nelle celle
- Controlla che l'encoding sia UTF-8

---

## 📊 METRICHE E MONITORAGGIO

### Cosa tenere traccia:

**Su Google Sheets:**
- Data ultima modifica (automatica)
- Numero totale record (formula: `=COUNTA(A:A)-1`)
- Chi ha modificato cosa (File → Cronologia versioni)

**Su GitHub:**
- Ogni commit = snapshot permanente
- Puoi vedere: chi, quando, cosa
- History completa di ogni modifica

### Statistiche utili:

Aggiungi un foglio "Statistiche" su Google Sheets con:
```
Totale pubblicazioni: =COUNTA(A:A)-1
Articoli in rivista: =COUNTIF(A:A,"articolo in rivista")
Articoli in volume: =COUNTIF(A:A,"articolo in volume miscellaneo")
Volumi miscellanei: =COUNTIF(A:A,"volume miscellaneo")
Monografie: =COUNTIF(A:A,"monografia")
Ultimo aggiornamento: =NOW()
```

---

## 🔐 BACKUP

### Backup automatici di Google Sheets:

**Opzione 1: Cronologia di Sheets** (gratis, limitato)
- Google Sheets salva automaticamente
- Puoi tornare indietro fino a 30 giorni (account gratuito)

**Opzione 2: Export manuale periodico** (consigliato)
- Ogni mese: Download → CSV
- Salva in cartella locale: `Backup_Bibliografia/2024-12-31.csv`
- Tieni ultimi 12 mesi

**Opzione 3: Script automatico** (avanzato)
- Te lo preparo se vuoi
- Esporta CSV ogni settimana su Drive
- Mantiene storico infinito

### Backup GitHub:

- ✅ GitHub = già un backup completo!
- ✅ Ogni commit = versione salvata per sempre
- ✅ Puoi clonare repository in locale quando vuoi

---

## ✅ CHECKLIST PRIMA DI PUBBLICARE

Prima di fare commit su GitHub, verifica:

- [ ] CSV esportato da Sheets (non da Excel)
- [ ] Rinominato correttamente: `bibliografia_cisui_completo.csv`
- [ ] Aperto e controllato visivamente (prime e ultime righe)
- [ ] Intestazioni presenti nella prima riga
- [ ] Nessuna riga completamente vuota
- [ ] (Opzionale) Testato in locale con server
- [ ] Messaggio commit descrittivo pronto

---

## 📞 CONTATTI E SUPPORTO

### Per i colleghi:

- Problemi con Google Sheets → [inserisci tuo contatto]
- Dubbi su come compilare → Consulta GUIDA_COMPILAZIONE.md
- Errori tecnici → [inserisci responsabile IT]

### Per te:

- Problemi GitHub → Documentazione GitHub
- Problemi script/HTML → [inserisci contatto supporto tecnico]
- Domande CSV/formato → Rileggi questa guida

---

## 🎓 RISORSE AGGIUNTIVE

- [Guida ufficiale Google Sheets](https://support.google.com/docs/answer/6000292)
- [Guida GitHub Pages](https://pages.github.com/)
- [Tutorial CSV](https://en.wikipedia.org/wiki/Comma-separated_values)

---

## 📝 LOG MODIFICHE

Tieni traccia degli aggiornamenti maggiori:

| Data | Modifiche | Record aggiunti | Note |
|------|-----------|-----------------|------|
| 2024-12-01 | Setup iniziale | 13 | Test con dati campione |
| [Data] | [Descrizione] | [N] | [Note] |

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** [Data]  
**Prossima revisione:** [Data + 6 mesi]
