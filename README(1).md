# Bibliografia CISUI - Sistema di Ricerca Online

Sistema di ricerca bibliografica interattivo per il Centro Interuniversitario Storia Università Italiane (CISUI) dell'Università di Bologna.

## 🎯 Caratteristiche

- **Ricerca avanzata** in tempo reale su titoli, autori, parole chiave e tag
- **Filtri multipli** per tipo documento, anno, campo di ricerca
- **Due formati di visualizzazione**: Standard e Chicago Manual of Style (17th ed.)
- **Export dei risultati** in CSV e TXT
- **Design responsive** compatibile con mobile e desktop
- **Stile istituzionale** UniBo con colori rosso bordeaux (#9d2235)

## 📚 Tipologie di documenti supportate

- Articoli in rivista
- Articoli in volume miscellaneo
- Volumi miscellanei
- Monografie

## 🚀 Come usare

### Installazione locale
1. Scarica il file `bibliografia_ricercabile.html`
2. Aprilo con qualsiasi browser moderno
3. Inizia subito a cercare!

### Integrazione in un sito web
```html
<!-- Opzione 1: iFrame -->
<iframe src="https://[tuo-username].github.io/[nome-repo]/bibliografia_ricercabile.html" 
        width="100%" 
        height="800px" 
        frameborder="0">
</iframe>

<!-- Opzione 2: Link diretto -->
<a href="https://[tuo-username].github.io/[nome-repo]/bibliografia_ricercabile.html" 
   target="_blank">
   Consulta la bibliografia
</a>
```

## 🔧 Personalizzazione

### Aggiungere nuove pubblicazioni
Modifica l'array `bibliographyData` nel file HTML:

```javascript
{
    title: "Titolo della pubblicazione",
    authors: "Cognome, Nome",
    year: 2024,
    type: "Articolo in rivista", // o "Articolo in volume", "Volume miscellaneo", "Monografia"
    publisher: "Nome editore/rivista",
    pages: "10-25",
    tags: ["Tag1", "Tag2"],
    keywords: "parole chiave per la ricerca",
    extra_info: "Informazioni aggiuntive (es. Vol. 12, In: Nome volume)"
}
```

### Modificare i colori
Cerca nel CSS le seguenti variabili di colore:
- `#9d2235` - Rosso bordeaux principale (UniBo)
- `#7a1a29` - Bordeaux scuro (hover)
- `#f5e6e9` - Rosa chiaro (sfondo tag)

### Aggiornare gli anni nel filtro
Modifica la sezione del filtro anno nell'HTML:
```html
<select id="yearFilter">
    <option value="">Tutti</option>
    <option value="2024">2024</option>
    <!-- Aggiungi altri anni -->
</select>
```

## 📖 Formato citazioni Chicago

Il sistema supporta automaticamente il Chicago Manual of Style (17th edition) con:
- Titoli di libri/riviste in corsivo
- Titoli di articoli tra virgolette
- Hanging indent (rientro sporgente)
- Punteggiatura conforme alle regole

## 🛠️ Requisiti tecnici

- Browser moderno (Chrome, Firefox, Safari, Edge)
- JavaScript abilitato
- Nessun server richiesto (funziona come file statico)

## 📱 Compatibilità

- ✅ Desktop (Windows, macOS, Linux)
- ✅ Tablet (iPad, Android)
- ✅ Mobile (iOS, Android)
- ✅ Tutti i browser moderni

## 📊 Dati attuali

La bibliografia contiene attualmente **13 pubblicazioni** del CISUI relative a:
- Storia delle università italiane
- Architettura universitaria
- Vita studentesca
- Politecnici
- Gruppi universitari fascisti

## 🔄 Aggiornamenti

Per aggiornare la bibliografia:
1. Modifica il file HTML
2. Commit su GitHub
3. Le modifiche saranno visibili automaticamente sul sito

## 📄 Licenza

Questo progetto è stato sviluppato per il CISUI - Centro Interuniversitario Storia Università Italiane.

## 🤝 Contatti

Per informazioni sul CISUI: https://centri.unibo.it/cisui/it

## 📝 Note tecniche

- File completamente standalone (non richiede librerie esterne)
- Nessun tracking o cookie
- Privacy-friendly (tutti i dati rimangono nel browser)
- Lightweight (~50KB)
- Velocità di ricerca istantanea

---

Sviluppato con ❤️ per il CISUI
