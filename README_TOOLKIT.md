# 📚 TOOLKIT COMPLETO BIBLIOGRAFIA CISUI

## 🎯 PANORAMICA

Questo toolkit contiene tutto il necessario per gestire la bibliografia CISUI con workflow ibrido Google Sheets + GitHub.

---

## 📦 CONTENUTI DEL PACCHETTO

### 📖 GUIDE E DOCUMENTAZIONE

1. **WORKFLOW_COMPLETO.md** ⭐ (inizia da qui!)
   - Guida completa del workflow
   - Setup iniziale Google Sheets
   - Processo di pubblicazione
   - Troubleshooting

2. **GUIDA_COLLEGHI_SEMPLICE.md**
   - Guida semplificata per i colleghi
   - Come aggiungere/modificare pubblicazioni
   - Esempi pratici
   - FAQ

3. **Questo file (README.md)**
   - Panoramica del toolkit
   - Quick start

### 🔧 FILE TECNICI (per conversione futura)

4. **converti_bibliografia.py**
   - Script Python per conversione Excel → CSV
   - Validazione automatica
   - Pulizia dati
   - Report dettagliati
   - ⚠️ DA ADATTARE quando ricevi file Excel definitivo

5. **converti_excel.bat** (Windows)
   - Wrapper user-friendly per lo script
   - Trascina e rilascia il file Excel
   - Installazione automatica dipendenze

### 🌐 FILE HTML E CSV (test con 13 record)

6. **bibliografia_ricercabile_completo.html**
   - Pagina web che legge da CSV
   - Stile CISUI
   - Ricerca e filtri
   - Export CSV/TXT
   - Chicago style

7. **bibliografia_cisui_completo.csv**
   - CSV di esempio con 13 record
   - Struttura completa (15 colonne)
   - Da sostituire con CSV completo

---

## 🚀 QUICK START

### 📝 FASE 1: Setup Google Sheets (ORA)

1. Leggi **WORKFLOW_COMPLETO.md** sezione "Setup Iniziale"
2. Crea Google Sheets
3. Importa `bibliografia_cisui_completo.csv` (file di esempio)
4. Configura validazione dati
5. Condividi con colleghi

### 👥 FASE 2: Lavoro Colleghi (QUOTIDIANO)

1. Colleghi leggono **GUIDA_COLLEGHI_SEMPLICE.md**
2. Aggiungono/modificano su Google Sheets
3. Ti avvisano quando hanno finito

### 🔍 FASE 3: Pubblicazione (SETTIMANALE)

1. Controlli Google Sheets
2. Export CSV
3. Carica su GitHub
4. Sito aggiornato in 2 minuti

---

## ⏳ PROSSIMI PASSI (quando ricevi file Excel completo)

### 1. Conversione Excel → CSV

Quando ti arriva il file Excel con migliaia di titoli:

```bash
# Windows:
converti_excel.bat bibliografia_completa.xlsx

# Mac/Linux:
python3 converti_bibliografia.py bibliografia_completa.xlsx bibliografia_cisui_completo.csv
```

Lo script:
- ✅ Valida la struttura
- ✅ Controlla tipologie
- ✅ Verifica anni
- ✅ Pulisce i dati
- ✅ Converte in CSV corretto

### 2. Importa in Google Sheets

1. Crea nuovo foglio
2. File → Importa → CSV appena creato
3. Applica formattazione (validazione dati, etc)
4. Condividi con team

### 3. Pubblica su GitHub

1. Carica `bibliografia_cisui_completo.csv` su GitHub
2. Carica `bibliografia_ricercabile_completo.html`
3. Attiva GitHub Pages
4. Testa su: `https://[username].github.io/[repo]/bibliografia_ricercabile_completo.html`

---

## 📋 CHECKLIST IMPLEMENTAZIONE

### Setup Iniziale (una tantum):
- [ ] Leggi WORKFLOW_COMPLETO.md
- [ ] Crea Google Sheets
- [ ] Importa CSV di esempio
- [ ] Configura validazione dati
- [ ] Proteggi intestazioni
- [ ] Condividi con colleghi
- [ ] Crea repository GitHub
- [ ] Attiva GitHub Pages
- [ ] Testa sito online

### Quando ricevi Excel completo:
- [ ] Esegui converti_bibliografia.py
- [ ] Verifica CSV generato
- [ ] Importa in Google Sheets
- [ ] Carica su GitHub
- [ ] Testa sito con dati completi
- [ ] Distribuisci GUIDA_COLLEGHI_SEMPLICE.md

---

## 🛠️ REQUISITI TECNICI

### Per usare il toolkit:

**Software necessario:**
- Python 3.6+ (per script conversione)
- pip (gestore pacchetti Python)
- pandas + openpyxl (installati automaticamente)

**Account/Servizi:**
- Account Google (per Sheets)
- Account GitHub (per hosting)

**Browser:**
- Chrome, Firefox, Safari, Edge (versioni recenti)

---

## 📁 STRUTTURA FILE FINALE

Quando tutto è pronto, avrai questa struttura:

```
Bibliografia CISUI/
├── 📊 Google Sheets (lavoro)
│   └── CISUI - Bibliografia Master
│
├── 💻 GitHub Repository
│   ├── bibliografia_ricercabile_completo.html
│   ├── bibliografia_cisui_completo.csv
│   ├── README.md
│   └── (altri file opzionali)
│
├── 📁 Locale (backup e guide)
│   ├── WORKFLOW_COMPLETO.md
│   ├── GUIDA_COLLEGHI_SEMPLICE.md
│   ├── converti_bibliografia.py
│   ├── converti_excel.bat
│   └── Backup/
│       ├── 2024-01-01.csv
│       ├── 2024-02-01.csv
│       └── ...
│
└── 🌐 Sito Pubblico
    └── https://[username].github.io/[repo]/
```

---

## 🔄 WORKFLOW QUOTIDIANO

```
MATTINA:
  Colleghi aprono Google Sheets
  Aggiungono nuove pubblicazioni
  Modificano record esistenti
  ↓
  Salvato automaticamente
  
QUANDO NECESSARIO:
  Colleghi ti avvisano: "Bibliografia aggiornata"
  ↓
  TU: Apri Google Sheets
  TU: Controllo rapido (5 min)
  TU: Export CSV
  TU: GitHub → Edit → Incolla → Commit
  ↓
  Sito aggiornato in 2 minuti! 🎉
```

---

## 📊 VANTAGGI DEL SISTEMA

| Aspetto | Soluzione |
|---------|-----------|
| **Facilità d'uso** | Google Sheets (familiare a tutti) |
| **Collaborazione** | Più persone contemporaneamente |
| **Controllo qualità** | Tu approvi prima della pubblicazione |
| **Versioning** | GitHub mantiene storia completa |
| **Sicurezza** | Errori non vanno online immediatamente |
| **Backup** | Google + GitHub + locale |
| **Accessibilità** | Sito pubblico 24/7 |
| **Performance** | HTML statico = velocissimo |
| **Costi** | Zero (tutto gratuito) |

---

## 🆘 SUPPORTO

### Hai problemi?

1. **Consulta le guide:**
   - WORKFLOW_COMPLETO.md (sezione Troubleshooting)
   - GUIDA_COLLEGHI_SEMPLICE.md (sezione "Ho fatto un errore")

2. **Verifica checklist:**
   - Setup corretto?
   - File nella stessa cartella?
   - GitHub Pages attivo?

3. **Test in locale:**
   - Prima di pubblicare, testa sempre in locale
   - Usa `avvia_server.bat` o `python3 -m http.server`

---

## 📝 NOTE IMPORTANTI

### ⚠️ ATTENZIONE:

1. **Script conversione è TEMPLATE**
   - Va adattato quando ricevi file Excel definitivo
   - Potrebbe servire modificare mapping colonne
   - Validazioni potrebbero richiedere aggiustamenti

2. **Prima pubblicazione online:**
   - Testa SEMPRE in locale prima
   - Verifica CSV con editor di testo
   - Controlla prime e ultime righe

3. **Backup regolari:**
   - Export CSV da Google Sheets ogni mese
   - Salva in cartella locale
   - GitHub è già un backup, ma ridondanza è meglio

---

## 🎓 RISORSE UTILI

- [Documentazione Google Sheets](https://support.google.com/docs)
- [Guida GitHub Pages](https://pages.github.com/)
- [Tutorial Python pandas](https://pandas.pydata.org/docs/)
- [Chicago Manual of Style](https://www.chicagomanualofstyle.org/)

---

## 📅 PROSSIMI AGGIORNAMENTI

Quando ricevi il file Excel definitivo:

1. ✉️ Mandamelo
2. 🔧 Adatto lo script di conversione
3. 🧪 Testiamo insieme
4. ✅ Sistema pronto per migliaia di titoli!

---

## 🎉 CONCLUSIONE

Hai ora un sistema completo per:
- ✅ Gestire migliaia di pubblicazioni
- ✅ Collaborare facilmente con colleghi
- ✅ Mantenere controllo qualità
- ✅ Pubblicare online in minuti
- ✅ Backup e versioning automatici

**Inizia con WORKFLOW_COMPLETO.md e sei pronto!** 🚀

---

**Versione toolkit:** 1.0 (Template - da adattare)  
**Data:** 2024  
**Contatto:** [inserire contatto per supporto]
