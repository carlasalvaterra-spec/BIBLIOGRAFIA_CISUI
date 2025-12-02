# 🚀 GUIDA COMPLETA: Caricare la Bibliografia su GitHub e Integrarla nel Sito CISUI

## 📋 INDICE
1. [Creare un account GitHub (se non ce l'hai)](#step-1)
2. [Creare un repository](#step-2)
3. [Caricare i file](#step-3)
4. [Attivare GitHub Pages](#step-4)
5. [Integrare nel sito CISUI](#step-5)

---

## <a name="step-1"></a>STEP 1: Creare un Account GitHub

### Se hai già un account GitHub, salta questo step!

1. Vai su [github.com](https://github.com)
2. Clicca su **Sign up** in alto a destra
3. Inserisci:
   - Email (usa quella istituzionale UniBo se possibile)
   - Password
   - Username (suggerimento: `cisui-unibo` o simile)
4. Verifica email
5. Completa il profilo (opzionale ma consigliato)

---

## <a name="step-2"></a>STEP 2: Creare un Repository

Un repository è come una cartella dove metti il tuo progetto.

### Procedura:

1. **Vai su GitHub** e fai login
2. Clicca sul **+** in alto a destra → **New repository**
3. **Compila i campi**:
   ```
   Repository name: bibliografia-cisui
   Description: Sistema di ricerca bibliografica del CISUI
   Public ✅ (deve essere pubblico per GitHub Pages)
   Add a README file: ✅ (spunta questa opzione)
   ```
4. Clicca su **Create repository**

🎉 Hai creato il repository!

---

## <a name="step-3"></a>STEP 3: Caricare i File

### Metodo A: Upload tramite interfaccia web (PIÙ SEMPLICE)

1. **Nel tuo repository appena creato**, clicca su **Add file** → **Upload files**
2. **Trascina** o clicca per selezionare:
   - `bibliografia_ricercabile.html`
   - `README.md` (opzionale, ma consigliato)
3. Nella casella "Commit changes" scrivi:
   ```
   Caricamento iniziale della bibliografia CISUI
   ```
4. Clicca su **Commit changes**

### Metodo B: Upload tramite Git (per utenti avanzati)

```bash
# Scarica Git se non ce l'hai: https://git-scm.com/

# 1. Clona il repository
git clone https://github.com/[tuo-username]/bibliografia-cisui.git
cd bibliografia-cisui

# 2. Copia i file nella cartella
# (copia bibliografia_ricercabile.html nella cartella)

# 3. Aggiungi, committa e carica
git add .
git commit -m "Caricamento iniziale della bibliografia"
git push origin main
```

---

## <a name="step-4"></a>STEP 4: Attivare GitHub Pages

GitHub Pages trasforma il tuo repository in un sito web accessibile pubblicamente!

### Procedura:

1. **Nel tuo repository**, clicca su **Settings** (⚙️ in alto)
2. Nel menu laterale sinistro, clicca su **Pages**
3. In **Source**, seleziona:
   ```
   Branch: main
   Folder: / (root)
   ```
4. Clicca su **Save**
5. **Aspetta 1-2 minuti** (GitHub deve costruire il sito)
6. Ricarica la pagina → vedrai un banner verde:
   ```
   Your site is live at https://[tuo-username].github.io/bibliografia-cisui/
   ```

🎉 Il tuo sito è online!

### URL finale:
```
https://[tuo-username].github.io/bibliografia-cisui/bibliografia_ricercabile.html
```

**Esempio concreto:**
Se il tuo username è `cisui-unibo`, l'URL sarà:
```
https://cisui-unibo.github.io/bibliografia-cisui/bibliografia_ricercabile.html
```

---

## <a name="step-5"></a>STEP 5: Integrare nel Sito CISUI

Ora devi integrare la bibliografia nel sito ufficiale del CISUI. Ci sono 3 metodi:

### 🔹 METODO 1: iFrame (CONSIGLIATO - Più semplice)

Inserisci questo codice nella pagina del sito CISUI dove vuoi mostrare la bibliografia:

```html
<iframe 
    src="https://[tuo-username].github.io/bibliografia-cisui/bibliografia_ricercabile.html" 
    width="100%" 
    height="900px" 
    frameborder="0"
    style="border: none; margin: 20px 0;">
</iframe>
```

**Vantaggi:**
- ✅ Facilissimo da implementare
- ✅ La bibliografia è sempre aggiornata automaticamente
- ✅ Non devi toccare il codice del sito CISUI

**Svantaggi:**
- ❌ Viene caricata in un iframe (tecnicamente è una pagina separata)

---

### 🔹 METODO 2: Link Diretto

Aggiungi semplicemente un link nel sito CISUI:

```html
<a href="https://[tuo-username].github.io/bibliografia-cisui/bibliografia_ricercabile.html" 
   target="_blank" 
   class="btn btn-primary">
   📚 Consulta la Bibliografia Ricercabile
</a>
```

**Vantaggi:**
- ✅ Semplicissimo
- ✅ La bibliografia si apre in una nuova finestra

**Svantaggi:**
- ❌ L'utente lascia il sito CISUI

---

### 🔹 METODO 3: Integrazione Diretta (Avanzato)

Se hai accesso al codice sorgente del sito CISUI:

1. **Copia il contenuto** di `bibliografia_ricercabile.html`
2. **Crea una nuova pagina** sul sito CISUI (es. `/bibliografia.html`)
3. **Incolla il codice**
4. **Adatta lo stile** se necessario per farlo combaciare con il resto del sito

**Vantaggi:**
- ✅ Totalmente integrata nel sito
- ✅ Stesso dominio
- ✅ Nessun iframe

**Svantaggi:**
- ❌ Richiede accesso al server/CMS del sito
- ❌ Gli aggiornamenti vanno fatti manualmente

---

## 📝 ESEMPIO PRATICO DI INTEGRAZIONE

### Se il sito CISUI usa WordPress:

1. Vai nella bacheca WordPress
2. **Pagine** → **Aggiungi nuova**
3. Titolo: "Bibliografia Ricercabile"
4. Passa alla modalità **HTML/Codice** (non Visuale)
5. Incolla:
```html
<iframe 
    src="https://[tuo-username].github.io/bibliografia-cisui/bibliografia_ricercabile.html" 
    width="100%" 
    height="900px" 
    frameborder="0"
    style="border: none;">
</iframe>
```
6. **Pubblica**
7. Aggiungi la pagina al menu di navigazione

### Se il sito CISUI è HTML statico:

1. Apri il file dove vuoi aggiungere la bibliografia (es. `pubblicazioni.html`)
2. Trova il punto dove vuoi inserirla
3. Aggiungi il codice iframe sopra
4. Salva e carica sul server

---

## 🔄 AGGIORNARE LA BIBLIOGRAFIA IN FUTURO

### Quando vuoi aggiungere nuove pubblicazioni:

#### Metodo Web (semplice):
1. Vai su GitHub nel tuo repository
2. Clicca su `bibliografia_ricercabile.html`
3. Clicca sull'icona **✏️ Edit** (matita)
4. Modifica l'array `bibliographyData` aggiungendo nuovi elementi
5. Scorri in basso → **Commit changes**
6. Scrivi un messaggio (es. "Aggiunte 5 nuove pubblicazioni")
7. Clicca **Commit changes**

**Entro 1-2 minuti le modifiche saranno visibili sul sito!** 🚀

#### Metodo Git (avanzato):
```bash
# 1. Clona se non l'hai già fatto
git clone https://github.com/[tuo-username]/bibliografia-cisui.git
cd bibliografia-cisui

# 2. Modifica il file localmente
# (apri bibliografia_ricercabile.html con un editor)

# 3. Committa e carica
git add bibliografia_ricercabile.html
git commit -m "Aggiunte nuove pubblicazioni"
git push origin main
```

---

## 🛠️ TROUBLESHOOTING

### ❓ "Il sito non si vede dopo aver attivato GitHub Pages"
- **Aspetta 2-5 minuti**, GitHub deve costruire il sito
- Controlla che il repository sia **pubblico** (non privato)
- Verifica che il file si chiami esattamente `bibliografia_ricercabile.html`

### ❓ "L'iframe non funziona nel sito CISUI"
- Alcuni CMS bloccano gli iframe per sicurezza
- Verifica nelle impostazioni di sicurezza del CMS
- Se bloccato, usa il Metodo 2 (link diretto) o Metodo 3 (integrazione diretta)

### ❓ "Voglio cambiare l'URL"
- Puoi usare un **dominio custom** (es. bibliografia.cisui.it)
- Nelle impostazioni GitHub Pages → **Custom domain**
- Richiede configurazione DNS (chiedi al responsabile IT UniBo)

### ❓ "Come faccio il backup?"
- GitHub È il backup! Tutti i file sono al sicuro
- Puoi clonare il repository in qualsiasi momento
- Opzionale: scarica periodicamente il file HTML

---

## 📊 STATISTICHE E MONITORAGGIO

### Vedere quante visite riceve la bibliografia:

GitHub non offre statistiche native, ma puoi:

1. **Google Analytics**: aggiungi il codice di tracking nel file HTML
2. **GitHub Insights**: Vai su Insights → Traffic (visite al repository)
3. **Servizi esterni**: Plausible, Matomo (privacy-friendly)

---

## 🔐 GESTIONE PERMESSI

### Collaboratori:

Se più persone devono aggiornare la bibliografia:

1. **Settings** → **Collaborators** → **Add people**
2. Inserisci username GitHub o email
3. Scegli permesso:
   - **Write** = può modificare
   - **Admin** = controllo totale

---

## ✨ FUNZIONALITÀ EXTRA OPZIONALI

### 1. Dominio personalizzato
```
bibliografia.cisui.it invece di github.io/...
```

### 2. HTTPS automatico
- GitHub Pages fornisce HTTPS gratuito
- Già attivo di default ✅

### 3. Versioning
- Ogni modifica è tracciata
- Puoi tornare a versioni precedenti
- Cronologia completa disponibile

### 4. Issues e Discussions
- Attiva **Issues** per ricevere segnalazioni di errori
- Attiva **Discussions** per feedback dagli utenti

---

## 🎓 RISORSE UTILI

- **Documentazione GitHub Pages**: https://pages.github.com/
- **Guida Git**: https://guides.github.com/
- **Supporto UniBo**: Se hai dubbi, contatta l'assistenza tecnica UniBo

---

## ✅ CHECKLIST FINALE

Prima di considerare il lavoro completato:

- [ ] Repository creato su GitHub
- [ ] File `bibliografia_ricercabile.html` caricato
- [ ] GitHub Pages attivato
- [ ] URL funzionante e testato
- [ ] Integrazione nel sito CISUI completata
- [ ] Test su desktop, tablet, mobile
- [ ] Backup locale del file (opzionale ma consigliato)
- [ ] Documentazione per futuri aggiornamenti

---

## 🆘 SERVE AIUTO?

### Contatti:
- **Supporto GitHub**: https://support.github.com/
- **Community UniBo**: Forum o mailing list del dipartimento
- **IT UniBo**: Assistenza tecnica dell'università

---

**🎉 Complimenti! La tua bibliografia è online e accessibile a tutti!**

---

*Ultima modifica: 2024-12-02*
