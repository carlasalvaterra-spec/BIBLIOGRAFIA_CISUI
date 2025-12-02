# 📝 GUIDA PER AGGIORNARE LA BIBLIOGRAFIA

## 🎯 Per i colleghi che devono aggiungere/modificare pubblicazioni

Questa guida spiega come aggiornare la bibliografia senza toccare il codice HTML!

---

## 📂 File da modificare: `bibliografia_cisui.csv`

Questo è l'unico file che dovete modificare per aggiornare la bibliografia.

---

## 🔧 METODO 1: Con Microsoft Excel (PIÙ SEMPLICE)

### Passo 1: Aprire il file
1. Fai doppio clic su `bibliografia_cisui.csv`
2. Si aprirà automaticamente con Excel

### Passo 2: Modificare i dati
- Ogni riga = 1 pubblicazione
- Ogni colonna = 1 informazione

### Colonne disponibili:
| Colonna | Cosa inserire | Esempio |
|---------|---------------|---------|
| **Titolo** | Titolo completo della pubblicazione | "Storia dell'Università di Bologna" |
| **Autori** | Cognome, Nome (separati da ; se più autori) | "Rossi, Mario; Bianchi, Luca" |
| **Anno** | Anno di pubblicazione (solo numero) | 2024 |
| **Tipo** | Tipo di documento (vedi sotto) | Articolo in rivista |
| **Editore** | Nome editore o rivista | Viella, Roma |
| **Pagine** | Numero pagine o intervallo | 10-25 oppure 300 |
| **Tag** | Categorie (separate da virgola) | Università, Storia |
| **Parole chiave** | Per la ricerca (tutto minuscolo) | storia università bologna |
| **Info aggiuntive** | Info extra come volume o "In:" | Vol. 12 |

### Tipi di documento accettati:
- `Articolo in rivista`
- `Articolo in volume`
- `Volume miscellaneo`
- `Monografia`

### Passo 3: Aggiungere una nuova pubblicazione
1. Vai all'ultima riga piena
2. Premi `TAB` per andare alla riga successiva
3. Compila tutte le colonne
4. **IMPORTANTE**: Se un campo contiene virgole, metti tutto tra virgolette: `"Titolo, con virgola"`

### Passo 4: Salvare
1. `File` → `Salva` (o Ctrl+S)
2. **IMPORTANTE**: Salva come `CSV UTF-8 (delimitato da virgole)`
3. Se Excel chiede conferma, clicca `Sì`

---

## 🔧 METODO 2: Con Google Sheets (COLLABORATIVO)

### Passo 1: Importare in Google Sheets
1. Vai su [sheets.google.com](https://sheets.google.com)
2. `File` → `Importa` → `Carica`
3. Seleziona `bibliografia_cisui.csv`
4. Clicca `Importa dati`

### Passo 2: Modificare online
- Più persone possono lavorare contemporaneamente
- Tutte le modifiche sono salvate automaticamente

### Passo 3: Esportare (quando hai finito)
1. `File` → `Scarica` → `Valori separati da virgola (.csv)`
2. Rinomina il file in `bibliografia_cisui.csv`
3. Sostituisci il vecchio file

---

## 🔧 METODO 3: Con un editor di testo (AVANZATO)

Se sei esperto, puoi modificare direttamente con Notepad++, VS Code, ecc.

**Attenzione**: 
- Rispetta il formato CSV
- Usa le virgolette per campi con virgole
- Mantieni l'intestazione (prima riga)

---

## ✅ ESEMPI PRATICI

### Esempio 1: Articolo in rivista
```csv
"Università e tecnologia","Verdi, Giuseppe",2024,Articolo in rivista,"«Rivista di Storia»","10-25","Università, Tecnologia","università tecnologia digitale",Vol. 15
```

### Esempio 2: Monografia
```csv
"Storia dell'Ateneo bolognese","Rossi, Maria",2023,Monografia,"Il Mulino, Bologna",450,"Storia, Bologna","storia università bologna ateneo","
```

### Esempio 3: Articolo in volume miscellaneo
```csv
"Architettura universitaria","Bianchi, Luca",2022,Articolo in volume,"Viella, Roma","45-78",Architettura,"architettura sedi universitarie","In: Neri, Paolo (a cura di), <i>Spazi del sapere</i>, Roma, Viella, 2022, pp. 300"
```

---

## ⚠️ ERRORI COMUNI DA EVITARE

### ❌ SBAGLIATO:
```csv
Storia dell'università (con problemi),Rossi Mario,2024,...
```
**Problema**: Virgola nel titolo senza virgolette, nome autore invertito

### ✅ GIUSTO:
```csv
"Storia dell'università (senza problemi)","Rossi, Mario",2024,...
```

---

### ❌ SBAGLIATO:
```csv
...,Università Storia,... 
```
**Problema**: Tag senza virgola tra loro

### ✅ GIUSTO:
```csv
...,"Università, Storia",...
```

---

### ❌ SBAGLIATO:
```csv
Titolo,Rossi,,2024,Articolo...
```
**Problema**: Campo vuoto (doppia virgola)

### ✅ GIUSTO:
```csv
Titolo,"Rossi, Mario",2024,Articolo...
```

---

## 🚀 CARICARE SU GITHUB (dopo le modifiche)

### Metodo Web (semplice):
1. Vai sul repository GitHub
2. Clicca su `bibliografia_cisui.csv`
3. Clicca sull'icona **✏️** (matita)
4. Copia e incolla il contenuto del tuo file aggiornato
5. Scorri in basso → **Commit changes**
6. Scrivi un messaggio (es. "Aggiunte 3 nuove pubblicazioni")
7. Clicca **Commit changes**

**Entro 1 minuto le modifiche saranno visibili online!** 🎉

### Metodo Upload (alternativo):
1. Vai sul repository GitHub
2. Clicca su `bibliografia_cisui.csv` 
3. Clicca sui tre puntini `...` in alto a destra
4. Clicca `Delete file`
5. Commit la cancellazione
6. Torna alla home del repository
7. `Add file` → `Upload files`
8. Trascina il nuovo `bibliografia_cisui.csv`
9. Commit

---

## 🧪 TESTARE LE MODIFICHE

Prima di caricare su GitHub, puoi testare in locale:

1. Salva `bibliografia_cisui.csv`
2. Apri `bibliografia_ricercabile_csv.html` nel browser
3. **Ricarica la pagina** (F5 o Ctrl+R)
4. Verifica che tutto funzioni
5. Se vedi errori, controlla il file CSV

---

## 📞 AIUTO?

### Problemi comuni:

**"Il sito non mostra le mie modifiche"**
- Hai salvato il CSV?
- Hai fatto il commit su GitHub?
- Hai aspettato 1-2 minuti?
- Prova a ricaricare la pagina (Ctrl+F5)

**"Vedo caratteri strani (à, è, ì)"**
- Salva come `CSV UTF-8` (non CSV normale)
- In Excel: `File` → `Salva con nome` → `CSV UTF-8`

**"La bibliografia non si carica"**
- Controlla che `bibliografia_cisui.csv` sia nella stessa cartella di `bibliografia_ricercabile_csv.html`
- Verifica che il nome del file sia esatto (minuscole/maiuscole)

---

## 📋 CHECKLIST PRIMA DI CARICARE

- [ ] Ho compilato tutti i campi obbligatori (Titolo, Autori, Anno, Tipo)
- [ ] Ho usato le virgolette per campi con virgole
- [ ] Ho usato il formato corretto per gli autori: "Cognome, Nome"
- [ ] Ho scelto un Tipo di documento dalla lista valida
- [ ] Ho separato i tag con virgole
- [ ] Ho testato in locale prima di caricare
- [ ] Ho salvato come CSV UTF-8

---

## 🎓 ESEMPIO COMPLETO

Ecco come appare una riga completa nel CSV:

```csv
"La nascita dell'Università moderna","Garin, Eugenio",2020,Monografia,"Laterza, Bari",356,"Storia, Università, Modernità","storia università moderna nascita garin",""
```

Quando viene visualizzata nel sito, apparirà così:

**Titolo**: La nascita dell'Università moderna  
**Autore**: Garin, Eugenio  
**Anno**: 2020  
**Tipo**: Monografia  
**Editore**: Laterza, Bari  
**Pagine**: 356  
**Tag**: Storia, Università, Modernità

---

**Buon lavoro! 📚**

*Per domande tecniche, contattare il responsabile IT o consultare la documentazione su GitHub.*
