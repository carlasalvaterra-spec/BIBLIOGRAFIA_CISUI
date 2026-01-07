# 📝 GUIDA RAPIDA PER COLLEGHI: Aggiornare la Bibliografia

## 🎯 Cosa devi sapere

Questa è una guida semplice e veloce per aggiungere o modificare pubblicazioni nella bibliografia CISUI usando Google Sheets.

**Non serve essere esperti!** Se sai usare Excel, sai usare questo. 😊

---

## 🔗 ACCESSO AL FOGLIO

**Link:** [Inserire link Google Sheets qui]

> ⚠️ Salva questo link nei preferiti!

---

## ➕ AGGIUNGERE UNA NUOVA PUBBLICAZIONE

### Passo 1: Vai all'ultima riga

Scorri fino in fondo al foglio e trova l'ultima riga con dati.

### Passo 2: Crea nuova riga

Clicca sulla riga successiva (quella vuota) e inizia a compilare.

### Passo 3: Compila i campi

#### 📋 Campi OBBLIGATORI (da compilare sempre):

| Colonna | Cosa scrivere | Esempio |
|---------|---------------|---------|
| **tipologia** | Usa menu a tendina 📥 | articolo in rivista |
| **anno** | Solo numero | 2024 |

#### 📝 Campi CONDIZIONALI (dipende dal tipo):

**Se è un ARTICOLO IN RIVISTA:**
- `autore_saggio` → Cognome, Nome
- `titolo_saggio` → Titolo completo
- `rivista` → Nome rivista (con «»)
- `annata` → Numero volume
- `pagine` → Intervallo (es: 10-25)

**Esempio:**
```
tipologia: articolo in rivista
autore_saggio: Rossi, Mario
titolo_saggio: La storia dell'università
rivista: «Annali di storia»
annata: 15
anno: 2024
pagine: 100-125
```

---

**Se è un ARTICOLO IN VOLUME MISCELLANEO:**
- `autore_saggio` → Cognome, Nome (autore articolo)
- `titolo_saggio` → Titolo articolo
- `autore_curatore_volume` → Cognome, Nome (curatore volume)
- `precisazione_curatore` → "a cura di" (usa tendina 📥)
- `titolo_volume` → Titolo volume completo
- `luogo` → Città
- `editore` → Casa editrice
- `pagine` → Intervallo pagine articolo

**Esempio:**
```
tipologia: articolo in volume miscellaneo
autore_saggio: Bianchi, Laura
titolo_saggio: L'architettura universitaria
autore_curatore_volume: Verdi, Giuseppe
precisazione_curatore: a cura di
titolo_volume: Studi sull'università italiana
luogo: Bologna
editore: Il Mulino
anno: 2023
pagine: 45-78
```

---

**Se è un VOLUME MISCELLANEO:**
- `autore_curatore_volume` → Cognome, Nome
- `precisazione_curatore` → "a cura di"
- `titolo_volume` → Titolo completo
- `luogo` → Città
- `editore` → Casa editrice
- `volumi` → Numero volumi (se più di 1)

**Esempio:**
```
tipologia: volume miscellaneo
autore_curatore_volume: Neri, Paolo
precisazione_curatore: a cura di
titolo_volume: Storia delle università italiane
luogo: Milano
editore: Franco Angeli
anno: 2024
volumi: 2
```

---

**Se è una MONOGRAFIA:**
- `autore_curatore_volume` → Cognome, Nome
- `titolo_volume` → Titolo completo
- `luogo` → Città
- `editore` → Casa editrice
- `pagine` → Numero pagine totali

**Esempio:**
```
tipologia: monografia
autore_curatore_volume: Ferrari, Anna
titolo_volume: L'università di Padova nel Rinascimento
luogo: Roma
editore: Carocci
anno: 2022
pagine: 450
```

---

## ✏️ MODIFICARE UNA PUBBLICAZIONE ESISTENTE

### Passo 1: Trova la riga

**Opzione A:** Scorri manualmente

**Opzione B:** Usa la ricerca
1. Premi **Ctrl+F** (Windows) o **Cmd+F** (Mac)
2. Scrivi parte del titolo o autore
3. Premi Invio

### Passo 2: Modifica

1. **Clicca sulla cella** da modificare
2. **Modifica** il contenuto
3. **Premi Invio** o clicca fuori

✅ **Salvato automaticamente!**

---

## ❌ ERRORI COMUNI DA EVITARE

### ⚠️ ATTENZIONE A:

**1. Non cancellare le intestazioni**
- La prima riga (in rosso) NON si tocca mai!

**2. Non cambiare l'ordine delle colonne**
- Le colonne devono rimanere nello stesso ordine

**3. Usa i menu a tendina quando disponibili**
- Per "tipologia" → usa la freccia 📥
- Per "precisazione_curatore" → usa la freccia 📥
- Questo evita errori di battitura

**4. Formato nomi autori**
- ✅ **Corretto:** Rossi, Mario
- ❌ **Sbagliato:** Mario Rossi
- ❌ **Sbagliato:** ROSSI MARIO

**5. Anno = solo numero**
- ✅ **Corretto:** 2024
- ❌ **Sbagliato:** duemila ventiquattro
- ❌ **Sbagliato:** 2024.0

**6. Campi vuoti**
- Se un campo non è applicabile, **lascialo vuoto**
- NON scrivere: "n/d", "N/A", "vuoto", "-"

---

## 🔍 COME CONTROLLARE SE HAI FATTO BENE

### Checklist veloce:

- [ ] Ho selezionato la tipologia dal menu a tendina?
- [ ] Ho inserito l'anno (solo numero)?
- [ ] Ho scritto autori nel formato: Cognome, Nome?
- [ ] Ho compilato tutti i campi obbligatori per quel tipo?
- [ ] Ho usato "(a cura di)" solo per i curatori?

---

## 🆘 HO FATTO UN ERRORE! COME LO SISTEMO?

### Se te ne accorgi subito:

**Opzione 1:** Premi **Ctrl+Z** (annulla)

**Opzione 2:** Modifica direttamente la cella

### Se te ne accorgi dopo:

**Opzione 1:** Correggi la cella sbagliata

**Opzione 2:** Se hai cancellato qualcosa per sbaglio:
1. **File → Cronologia delle versioni → Vedi cronologia**
2. Cerca la versione corretta
3. **Ripristina questa versione**

### Se hai cancellato tutto per sbaglio:

😱 **NON FARTI PRENDERE DAL PANICO!**

1. Contatta immediatamente [inserire responsabile]
2. Google Sheets salva tutto automaticamente
3. Si può recuperare dalla cronologia

---

## 💡 CONSIGLI PRATICI

### Trucchetti utili:

**1. Copia-incolla da record simile**
- Se devi aggiungere tanti articoli della stessa rivista
- Copia una riga esistente
- Modifica solo i campi diversi

**2. Usa Ctrl+D per riempire in basso**
- Compila un campo (es: anno = 2024)
- Seleziona quella cella + celle vuote sotto
- Premi Ctrl+D → riempie tutte con lo stesso valore

**3. Filtri per verificare**
- Clicca sulla freccia nelle intestazioni
- Vedi solo certi tipi di pubblicazioni
- Utile per controllare coerenza

**4. Commenti per comunicare**
- Tasto destro su cella → Inserisci commento
- Scrivi note per colleghi
- Esempio: "Verificare editore"

---

## 📅 QUANDO PUBBLICARE LE MODIFICHE

### Il tuo lavoro su Google Sheets:

✅ **Salvataggio:** Automatico (ogni pochi secondi)

✅ **Visibilità colleghi:** Immediata (vedono le tue modifiche in tempo reale)

✅ **Pubblicazione online (sito CISUI):** NON immediata

### Come funziona la pubblicazione:

```
1. Tu lavori su Google Sheets ────┐
2. Altri colleghi vedono subito   │
3. Tutti aggiungete/modificate    │
4. Quando avete finito...          │
5. Mandate messaggio a [responsabile]
6. [Responsabile] controlla        │
7. [Responsabile] pubblica su GitHub
8. Sito si aggiorna (2 minuti)    │
```

**In pratica:** Non preoccuparti della pubblicazione, qualcun altro se ne occupa! 😊

---

## 🎓 ESEMPI COMPLETI

### Esempio 1: Articolo in rivista

Vuoi aggiungere: Mario Rossi ha pubblicato "Università e società" nella rivista "Annali di storia" nel 2024, volume 20, pagine 50-75.

**Compila così:**
```
tipologia: articolo in rivista
autore_saggio: Rossi, Mario
titolo_saggio: Università e società
rivista: «Annali di storia»
annata: 20
anno: 2024
pagine: 50-75
```

### Esempio 2: Libro curato

Vuoi aggiungere: Laura Bianchi ha curato il volume "Storia dell'ateneo bolognese" per Il Mulino, Bologna, 2023, 500 pagine.

**Compila così:**
```
tipologia: volume miscellaneo
autore_curatore_volume: Bianchi, Laura
precisazione_curatore: a cura di
titolo_volume: Storia dell'ateneo bolognese
luogo: Bologna
editore: Il Mulino
anno: 2023
pagine: 500
```

### Esempio 3: Articolo in volume

Vuoi aggiungere: Giuseppe Verdi ha scritto "L'architettura delle sedi" (pagg. 100-150) nel volume curato da Paolo Neri "Università italiane", Carocci, Roma, 2022.

**Compila così:**
```
tipologia: articolo in volume miscellaneo
autore_saggio: Verdi, Giuseppe
titolo_saggio: L'architettura delle sedi
autore_curatore_volume: Neri, Paolo
precisazione_curatore: a cura di
titolo_volume: Università italiane
luogo: Roma
editore: Carocci
anno: 2022
pagine: 100-150
```

---

## 📞 SERVE AIUTO?

### Contatti:

- **Dubbi su come compilare:** [inserire contatto]
- **Problemi tecnici con Sheets:** [inserire contatto IT]
- **Errori da correggere:** [inserire responsabile]

### Risorse:

- **Questa guida:** [Link a questa guida]
- **Guida Google Sheets:** https://support.google.com/docs
- **Video tutorial:** [Se disponibile]

---

## ✅ CHECKLIST FINALE

Prima di chiudere, verifica:

- [ ] Ho compilato tutti i campi obbligatori
- [ ] Ho usato i menu a tendina dove disponibili
- [ ] Il formato nomi è: Cognome, Nome
- [ ] L'anno è un numero
- [ ] Non ho cancellato le intestazioni
- [ ] Ho salvato (automatico, ma controlla che non ci siano errori rossi)

---

**🎉 OTTIMO LAVORO!**

Le tue modifiche sono salvate e i colleghi possono già vederle.

Quando tutti avranno finito di aggiungere pubblicazioni, il responsabile pubblicherà l'aggiornamento sul sito.

---

**Versione guida:** 1.0  
**Per problemi o suggerimenti:** [inserire contatto]
