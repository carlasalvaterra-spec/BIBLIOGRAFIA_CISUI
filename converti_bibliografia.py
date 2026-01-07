#!/usr/bin/env python3
"""
Script di conversione Excel → CSV per Bibliografia CISUI
Versione: 1.0 TEMPLATE (da adattare quando ricevi file definitivo)

COSA FA:
1. Legge file Excel con migliaia di titoli
2. Valida la struttura delle colonne
3. Pulisce i dati (spazi, caratteri strani)
4. Converte in CSV formato corretto per l'HTML
5. Genera report di conversione

USO:
    python converti_bibliografia.py input.xlsx output.csv
"""

import pandas as pd
import sys
import os
from datetime import datetime

# ============================================================================
# CONFIGURAZIONE - MODIFICA QUESTI VALORI QUANDO HAI IL FILE DEFINITIVO
# ============================================================================

# Nomi colonne attese nel file Excel originale
COLONNE_EXCEL = [
    'tipologia',
    'autore saggio',
    'precisazione autore',
    'titolo saggio',
    'autore o curatore volume',
    'precisazione autore o curatore volume',
    'titolo volume',
    'luogo',
    'editore',
    'data',
    'volumi',
    'rivista',
    'annata',
    'fascicolo',
    'pagine'
]

# Nomi colonne per il CSV finale (senza spazi)
COLONNE_CSV = [
    'tipologia',
    'autore_saggio',
    'precisazione_autore',
    'titolo_saggio',
    'autore_curatore_volume',
    'precisazione_curatore',
    'titolo_volume',
    'luogo',
    'editore',
    'anno',
    'volumi',
    'rivista',
    'annata',
    'fascicolo',
    'pagine'
]

# Valori validi per tipologia
TIPOLOGIE_VALIDE = [
    'articolo in rivista',
    'articolo in volume miscellaneo',
    'volume miscellaneo',
    'monografia'
]

# ============================================================================
# FUNZIONI DI VALIDAZIONE
# ============================================================================

def valida_struttura(df):
    """Verifica che il DataFrame abbia le colonne corrette"""
    print("\n🔍 Validazione struttura file...")
    
    colonne_presenti = df.columns.tolist()
    colonne_mancanti = [col for col in COLONNE_EXCEL if col not in colonne_presenti]
    colonne_extra = [col for col in colonne_presenti if col not in COLONNE_EXCEL]
    
    if colonne_mancanti:
        print(f"   ⚠️  ATTENZIONE: Colonne mancanti: {colonne_mancanti}")
        return False
    
    if colonne_extra:
        print(f"   ℹ️  Info: Colonne extra trovate (verranno ignorate): {colonne_extra}")
    
    print("   ✅ Struttura OK!")
    return True

def valida_tipologie(df):
    """Verifica che le tipologie siano valide"""
    print("\n🔍 Validazione tipologie...")
    
    tipologie_uniche = df['tipologia'].dropna().unique()
    tipologie_invalide = [t for t in tipologie_uniche if t not in TIPOLOGIE_VALIDE]
    
    if tipologie_invalide:
        print(f"   ⚠️  ATTENZIONE: Tipologie non valide trovate:")
        for tip in tipologie_invalide:
            count = len(df[df['tipologia'] == tip])
            print(f"      - '{tip}' ({count} occorrenze)")
        print(f"\n   Tipologie valide: {TIPOLOGIE_VALIDE}")
        return False
    
    print("   ✅ Tipologie OK!")
    return True

def valida_anni(df):
    """Verifica che gli anni siano validi"""
    print("\n🔍 Validazione anni...")
    
    anni_validi = []
    anni_invalidi = []
    
    for idx, anno in df['data'].items():
        if pd.isna(anno):
            anni_invalidi.append((idx, anno, "Anno mancante"))
        elif not isinstance(anno, (int, float)):
            anni_invalidi.append((idx, anno, "Anno non numerico"))
        elif anno < 1000 or anno > 2100:
            anni_invalidi.append((idx, anno, "Anno fuori range"))
        else:
            anni_validi.append(anno)
    
    if anni_invalidi:
        print(f"   ⚠️  ATTENZIONE: {len(anni_invalidi)} record con anno invalido")
        print(f"   Primi 5 esempi:")
        for idx, anno, motivo in anni_invalidi[:5]:
            print(f"      - Riga {idx+2}: '{anno}' ({motivo})")
        
        risposta = input(f"\n   Continuare comunque? (s/n): ")
        if risposta.lower() != 's':
            return False
    else:
        print("   ✅ Anni OK!")
    
    return True

# ============================================================================
# FUNZIONI DI PULIZIA
# ============================================================================

def pulisci_testo(testo):
    """Pulisce una stringa (rimuove spazi extra, etc)"""
    if pd.isna(testo) or testo == '':
        return ''
    
    # Converti in stringa
    testo = str(testo)
    
    # Rimuovi spazi multipli
    testo = ' '.join(testo.split())
    
    # Rimuovi spazi iniziali/finali
    testo = testo.strip()
    
    return testo

def pulisci_dataframe(df):
    """Pulisce tutti i campi di testo nel DataFrame"""
    print("\n🧹 Pulizia dati...")
    
    colonne_testo = [
        'tipologia', 'autore saggio', 'titolo saggio',
        'autore o curatore volume', 'precisazione autore o curatore volume',
        'titolo volume', 'luogo', 'editore', 'rivista', 'pagine'
    ]
    
    for col in colonne_testo:
        if col in df.columns:
            df[col] = df[col].apply(pulisci_testo)
    
    # Sostituisci NaN con stringhe vuote
    df = df.fillna('')
    
    print("   ✅ Dati puliti!")
    return df

# ============================================================================
# FUNZIONE PRINCIPALE DI CONVERSIONE
# ============================================================================

def converti_excel_a_csv(file_input, file_output):
    """
    Converte file Excel in CSV formato CISUI
    
    Args:
        file_input: path al file Excel
        file_output: path al file CSV da creare
    """
    
    print("="*80)
    print("CONVERSIONE BIBLIOGRAFIA CISUI: Excel → CSV")
    print("="*80)
    
    # 1. LETTURA FILE
    print(f"\n📂 Lettura file: {file_input}")
    try:
        df = pd.read_excel(file_input)
        print(f"   ✅ File letto: {len(df)} record trovati")
    except Exception as e:
        print(f"   ❌ ERRORE nella lettura: {e}")
        return False
    
    # 2. VALIDAZIONE
    if not valida_struttura(df):
        print("\n❌ ERRORE: Struttura file non valida!")
        return False
    
    if not valida_tipologie(df):
        print("\n❌ ERRORE: Tipologie non valide!")
        return False
    
    if not valida_anni(df):
        print("\n❌ ERRORE: Anni non validi!")
        return False
    
    # 3. PULIZIA
    df = pulisci_dataframe(df)
    
    # 4. RINOMINA COLONNE
    print("\n🔄 Rinomina colonne...")
    mapping_colonne = dict(zip(COLONNE_EXCEL, COLONNE_CSV))
    df = df.rename(columns=mapping_colonne)
    
    # Seleziona solo le colonne che ci servono (nell'ordine corretto)
    df = df[COLONNE_CSV]
    print("   ✅ Colonne rinominate!")
    
    # 5. STATISTICHE
    print("\n📊 STATISTICHE:")
    print(f"   Totale record: {len(df)}")
    print(f"\n   Distribuzione per tipologia:")
    for tip in TIPOLOGIE_VALIDE:
        count = len(df[df['tipologia'] == tip])
        if count > 0:
            print(f"      - {tip}: {count}")
    
    print(f"\n   Range anni:")
    anni = df['anno'].dropna()
    if len(anni) > 0:
        print(f"      - Dal {int(anni.min())} al {int(anni.max())}")
    
    # 6. SALVATAGGIO
    print(f"\n💾 Salvataggio CSV: {file_output}")
    try:
        df.to_csv(file_output, index=False, encoding='utf-8')
        print(f"   ✅ CSV creato con successo!")
        
        # Verifica dimensione file
        dimensione = os.path.getsize(file_output) / 1024  # KB
        print(f"   📦 Dimensione file: {dimensione:.2f} KB")
        
    except Exception as e:
        print(f"   ❌ ERRORE nel salvataggio: {e}")
        return False
    
    # 7. REPORT FINALE
    print("\n" + "="*80)
    print("✅ CONVERSIONE COMPLETATA CON SUCCESSO!")
    print("="*80)
    print(f"\n📄 File CSV creato: {file_output}")
    print(f"📊 Record totali: {len(df)}")
    print(f"📅 Data conversione: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n📋 PROSSIMI PASSI:")
    print("   1. Apri il CSV con un editor di testo per verificare")
    print("   2. Testa in locale con bibliografia_ricercabile_completo.html")
    print("   3. Se tutto ok, carica su GitHub")
    
    return True

# ============================================================================
# FUNZIONE DI HELP
# ============================================================================

def mostra_help():
    """Mostra le istruzioni d'uso"""
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                SCRIPT CONVERSIONE BIBLIOGRAFIA CISUI                        ║
╚════════════════════════════════════════════════════════════════════════════╝

USO:
    python converti_bibliografia.py <file_input.xlsx> <file_output.csv>

ESEMPI:
    python converti_bibliografia.py bibliografia_completa.xlsx bibliografia_cisui_completo.csv
    python converti_bibliografia.py dati.xlsx output.csv

REQUISITI:
    - Python 3.6+
    - pandas installato (pip install pandas openpyxl)

COSA FA:
    ✓ Legge file Excel con bibliografia completa
    ✓ Valida struttura e contenuti
    ✓ Pulisce i dati
    ✓ Converte in formato CSV corretto per HTML
    ✓ Genera report di conversione

STRUTTURA EXCEL RICHIESTA:
    Le colonne devono essere esattamente queste (in qualsiasi ordine):
    - tipologia
    - autore saggio
    - precisazione autore
    - titolo saggio
    - autore o curatore volume
    - precisazione autore o curatore volume
    - titolo volume
    - luogo
    - editore
    - data
    - volumi
    - rivista
    - annata
    - fascicolo
    - pagine

TIPOLOGIE VALIDE:
    - articolo in rivista
    - articolo in volume miscellaneo
    - volume miscellaneo
    - monografia

NOTE:
    - Il file Excel può avere migliaia di righe
    - Le righe vuote vengono ignorate
    - Gli errori vengono segnalati ma la conversione continua

Per problemi o domande: [inserire contatto]
    """)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Controlla argomenti
    if len(sys.argv) != 3:
        mostra_help()
        sys.exit(1)
    
    file_input = sys.argv[1]
    file_output = sys.argv[2]
    
    # Verifica che il file input esista
    if not os.path.exists(file_input):
        print(f"❌ ERRORE: File non trovato: {file_input}")
        sys.exit(1)
    
    # Verifica che il file input sia Excel
    if not file_input.endswith(('.xlsx', '.xls')):
        print(f"❌ ERRORE: Il file deve essere Excel (.xlsx o .xls)")
        sys.exit(1)
    
    # Esegui conversione
    successo = converti_excel_a_csv(file_input, file_output)
    
    # Exit code
    sys.exit(0 if successo else 1)
